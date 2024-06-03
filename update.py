import yaml
import os

cwd = os.getcwd()
print("Current working directory:", cwd)

with open('./feeds.yaml', 'r') as f:
    data = yaml.safe_load(f)
    repos = data.get('repositories', [])
    repo_names = []
    for repo in repos:
        name = repo['name']
        repo_names.append(name)
        print(f"::set-output name={name}_url::{repo['url']}")
        print(f"::set-output name={name}_path::{repo['path']}")
    
    # 输出所有仓库名称，以空格分隔
    print(f"::set-output name=repo_names::{' '.join(repo_names)}")
