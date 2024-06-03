import yaml

with open('./feed.yaml', 'r') as f:
    data = yaml.safe_load(f)
    repos = data.get('repositories', [])
    for repo in repos:
        print(f"::set-output name={repo['name']}_url::{repo['url']}")
        print(f"::set-output name={repo['name']}_path::{repo['path']}")
