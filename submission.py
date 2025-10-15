import requests
import subprocess

# ---- FILL THESE WITH YOUR DATA ----
email = "23f2002518@ds.study.iitm.ac.in"      # Your IITM email address
task = "your-task-id"                         # Task value from the assignment/request
round_num = 1                                 # Round number, usually 1
nonce = "your-nonce-value"                    # Nonce from the request
repo_url = "https://github.com/ray-sachin/llm-project-1"
pages_url = "https://ray-sachin.github.io/llm-project-1/"

evaluation_url = "https://..."                # Paste the evaluation_url value from your assignment/request

# ---- Do not edit below unless you want to change logic ----
commit_sha = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()

payload = {
    "email": email,
    "task": task,
    "round": round_num,
    "nonce": nonce,
    "repo_url": repo_url,
    "commit_sha": commit_sha,
    "pages_url": pages_url
}

resp = requests.post(evaluation_url, json=payload)
print("Status:", resp.status_code)
try:
    print("Response:", resp.json())
except Exception:
    print("Raw Response:", resp.text)
