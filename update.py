import yaml
import os
cwd = os.getcwd()
print("Current working directory:", cwd)

with open('./feeds.yaml', 'r') as f:
    data = yaml.safe_load(f)
    repos = data.get('repositories', [])
    for repo in repos:
        print(f"::set-output name={repo['name']}_url::{repo['url']}")
        print(f"::set-output name={repo['name']}_path::{repo['path']}")
