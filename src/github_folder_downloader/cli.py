import argparse
import os
import sys
import requests
from urllib.parse import urlparse

API_BASE = "https://api.github.com"

def parse_repo_url(repo_url):
    """
    Parses a GitHub repository URL that may include branch and subfolder information.
    Expected formats:
      - https://github.com/owner/repo
      - https://github.com/owner/repo/tree/branch
      - https://github.com/owner/repo/tree/branch/subpath
    Returns a tuple (owner, repo, branch, subpath) where branch defaults to "main" and subpath defaults to "" if not provided.
    """
    parsed = urlparse(repo_url)
    path_parts = parsed.path.strip("/").split("/")
    if len(path_parts) < 2:
        sys.exit("Invalid repository URL. Expected format: https://github.com/owner/repo")
    owner, repo = path_parts[0], path_parts[1]
    if repo.endswith(".git"):
        repo = repo[:-4]
    branch = "main"
    subpath = ""
    # If the URL contains 'tree', extract branch and subfolder from it.
    if len(path_parts) >= 4 and path_parts[2] == "tree":
        branch = path_parts[3]
        if len(path_parts) > 4:
            subpath = "/".join(path_parts[4:])
    return owner, repo, branch, subpath

def get_repo_contents(owner, repo, path="", branch="main"):
    """
    Recursively retrieves repository contents using the GitHub API.
    """
    url = f"{API_BASE}/repos/{owner}/{repo}/contents/{path}"
    params = {"ref": branch}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        sys.exit(f"Error fetching contents from GitHub API: {response.status_code} {response.text}")
    return response.json()

def download_file(raw_url, local_path):
    """
    Downloads a single file from the given raw URL to local_path.
    """
    response = requests.get(raw_url)
    if response.status_code != 200:
        print(f"Failed to download file: {raw_url}", file=sys.stderr)
        return
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    with open(local_path, "wb") as f:
        f.write(response.content)
    print(f"Downloaded: {local_path}")

def process_contents(contents, owner, repo, output_dir, branch):
    """
    Processes the contents returned from get_repo_contents.
    """
    for item in contents:
        item_type = item.get("type")
        item_path = item.get("path")
        if item_type == "dir":
            # Recursively process directory
            sub_contents = get_repo_contents(owner, repo, item_path, branch)
            process_contents(sub_contents, owner, repo, output_dir, branch)
        elif item_type == "file":
            # Get the raw file URL.
            raw_url = item.get("download_url")
            local_file_path = os.path.join(output_dir, item_path)
            download_file(raw_url, local_file_path)
        else:
            print(f"Skipping unknown type: {item.get('type')} at {item_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Download folders from GitHub repositories without zipping."
    )
    parser.add_argument(
        "repo_url", 
        help="The GitHub repository URL (e.g., https://github.com/owner/repo)"
    )
    parser.add_argument(
        "output_dir",
        help="The output directory to save the downloaded files."
    )
    parser.add_argument(
        "--branch", default="main",
        help="The branch to download from (default: main)."
    )
    parser.add_argument(
        "--subpath", default="",
        help="The repository sub-path to download (default: root)."
    )
    args = parser.parse_args()
    
    owner, repo, branch, subpath = parse_repo_url(args.repo_url)
    print(f"Processing repository '{owner}/{repo}' on branch '{branch}' with subfolder '{subpath}'...")
    
    contents = get_repo_contents(owner, repo, path=subpath, branch=branch)
    process_contents(contents, owner, repo, args.output_dir, branch)
    print("Download complete.")

if __name__ == "__main__":
    main()