import yaml
import json
import os

cwd = os.getcwd()
print("Current working directory:", cwd)

with open('./feeds.yaml', 'r') as f:
    data = yaml.safe_load(f)
    repos = data.get('repositories', [])
    repos_output = []

    for repo in repos:
        repos_output.append({
            "name": repo['name'],
            "url": repo['url'],
            "path": repo['path']
        })

    # 将仓库信息转换为 JSON 字符串并写入文件
    with open('repos.json', 'w') as json_file:
        json.dump(repos_output, json_file)
    print("Repositories information has been written to repos.json")
