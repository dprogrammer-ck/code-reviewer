import re
from collections import defaultdict
from typing import Dict, List

def extract_diff_line_map(diffs: List[Dict]) -> Dict[str, List[int]]:
    line_map = defaultdict(list)

    for diff in diffs:
        filename = diff["filename"]
        patch = diff.get("patch", "")
        current_line = None
        line_offset = 0

        for line in patch.splitlines():
            if line.startswith("@@"):
                match = re.match(r"@@ -\d+(?:,\d+)? \+(\d+)", line)
                if match:
                    current_line = int(match.group(1))
                    line_offset = 0
            elif line.startswith("+") and not line.startswith("+++"):
                if current_line is not None:
                    line_map[filename].append(current_line + line_offset)
                line_offset += 1
            elif not line.startswith("-"):
                line_offset += 1

    return dict(line_map)
