import json
import os
import tempfile
from git import Repo

def lambda_handler(event, context):
    gitlab_url = event['gitlab_url']
    file_path = event['file_path']
    access_token = event.get('access_token')  # Optional if the repo is public

    # Print the GitLab repo URL
    print(f"GitLab repository URL: {gitlab_url}")

    # Create a temporary directory to clone the repo
    with tempfile.TemporaryDirectory() as temp_dir:
        repo_dir = os.path.join(temp_dir, 'repo')
        
        # Clone the repository
        if access_token:
            clone_url = gitlab_url.replace("https://", f"https://oauth2:{access_token}@")
            Repo.clone_from(clone_url, repo_dir)
        else:
            Repo.clone_from(gitlab_url, repo_dir)

        target_file = os.path.join(repo_dir, file_path)
        if not os.path.exists(target_file):
            return {
                'statusCode': 404,
                'body': json.dumps(f"File {file_path} not found in the repository.")
            }

        with open(target_file, 'r') as file:
            file_content = file.read()

        # Print the file path
        print(f"File path: {file_path}")

        return {
            'statusCode': 200,
            'body': json.dumps({
                'file_path': file_path,
                'file_content': file_content
            })
        }
