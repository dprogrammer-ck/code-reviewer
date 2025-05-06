from api.github_pr_fetcher import GitHubPRFetcher
from dotenv import load_dotenv
import os

load_dotenv()  

token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
repo = os.getenv("GITHUB_REPO") or "dprogrammer-ck/code-reviewer"
pr_number = 1  # Test PR number

fetcher = GitHubPRFetcher(token, repo)
pr_data = fetcher.get_pull_request(pr_number)

for d in pr_data["diffs"]:
    print(f"\n📄 File: {d['filename']}\n---\n{d['patch']}")
