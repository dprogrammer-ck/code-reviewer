import os
import subprocess
import xml.etree.ElementTree as ET
from typing import List, Dict
from utils.pmd_util import detect_language, get_ruleset_path
from utils.diff_parser import extract_diff_line_map

def run_pmd(file_path: str, ruleset_path: str, pmd_cmd: str = "pmd") -> str:
    output_path = f"/tmp/pmd_output_{os.path.basename(file_path)}.xml"
    subprocess.run([
        pmd_cmd, "check", "-d", file_path,
        "-R", ruleset_path, "-f", "xml", "-r", output_path
    ], check=True)
    return output_path

def parse_pmd_output(xml_path: str) -> List[Dict]:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    results = []

    for file_tag in root.findall("file"):
        for v in file_tag.findall("violation"):
            results.append({
                "file": file_tag.attrib["name"],
                "line": int(v.attrib["beginline"]),
                "rule": v.attrib["rule"],
                "message": v.text.strip()
            })
    return results

def filter_by_diff(violations: List[Dict], diff_map: Dict[str, List[int]]) -> List[Dict]:
    filtered = []
    for v in violations:
        relative = os.path.relpath(v["file"])
        if relative in diff_map and v["line"] in diff_map[relative]:
            filtered.append(v)
    return filtered

def process_files_with_pmd(diffs: List[Dict], diff_only: bool = True) -> List[Dict]:
    violations = []
    diff_map = extract_diff_line_map(diffs)

    for f in diffs:
        filename = f["filename"]
        if not os.path.exists(filename): continue
        lang = detect_language(filename)
        if not lang: continue

        ruleset = get_ruleset_path(lang)
        try:
            xml_path = run_pmd(filename, ruleset)
            file_violations = parse_pmd_output(xml_path)
            filtered = filter_by_diff(file_violations, diff_map) if diff_only else file_violations
            violations.extend(filtered)
        except subprocess.CalledProcessError:
            print(f"[!] PMD failed for {filename}")

    return violations
