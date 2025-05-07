import os

def detect_language(filename: str) -> str:
    ext = os.path.splitext(filename)[1].lower()
    return {
        ".java": "java",
        ".js": "javascript",
        ".cls": "apex",
    }.get(ext, "")

def get_ruleset_path(language: str) -> str:
    ruleset_relative_path = f"pmd-rules/{language}/quickstart.xml"
    return os.path.abspath(ruleset_relative_path)
