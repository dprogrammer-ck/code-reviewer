import requests

def parse_pr_url(url: str):
    # https://github.com/owner/repo/pull/42
    parts = url.strip().split('/')
    return parts[3], parts[4], int(parts[-1])

def get_pr_diff(owner: str, repo: str, pr_number: int):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"
    headers = {
        "Accept": "application/vnd.github.v3.diff"
    }
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        return res.text
    else:
        raise Exception(f"Failed to fetch diff: {res.status_code}")


url = "https://github.com/openai/openai-python/pull/42"
owner, repo, pr_number = parse_pr_url(url)
diff = get_pr_diff(owner, repo, pr_number)

print(diff[:500])  