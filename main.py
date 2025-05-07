from api.github_pr_fetcher import GitHubPRFetcher
from dotenv import load_dotenv
import os
from pr_reviewer.pmd_runner import process_files_with_pmd

load_dotenv()  

token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
repo = os.getenv("GITHUB_REPO") or "dprogrammer-ck/code-reviewer"
pr_number = 1  # Test PR number

fetcher = GitHubPRFetcher(token, repo)
pr_data = fetcher.get_pull_request(pr_number)

for d in pr_data["diffs"]:
    print(f"\n📄 File: {d['filename']}\n---\n{d['patch']}")

violations = process_files_with_pmd(pr_data["diffs"], diff_only=False)
# 🧾 Display violations in clean output
print("\n📌 PMD Violations (Diff Only):\n")
for v in violations:
    print(f"🧨 {v['file']}:{v['line']} - {v['rule']}")
    print(f"   💬 {v['message']}")
    print("--------------------------------------------------")

if not violations:
    print("✅ No PMD violations found in changed lines.")