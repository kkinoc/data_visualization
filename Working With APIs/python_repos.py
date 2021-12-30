import requests

# Make an API call and store the response.
filename = "data/github_info.txt"
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code:  {r.status_code}")

# Store API response in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
words = "Information about each github repository:\n"
# Examine the first repository.
for repo in range(len(repo_dicts)):
    repo_dict = repo_dicts[repo]

    with open(filename, 'w', encoding="utf-8") as f:
        words += f"\nSelected information about repository {repo+1} \n" \
                 f"Name: {repo_dict['name']}\n" \
                 f"Owner: {repo_dict['owner']['login']}\n" \
                 f"Stars: {repo_dict['stargazers_count']}\n" \
                 f"Repository: {repo_dict['html_url']}\n" \
                 f"Created: {repo_dict['created_at']}\n" \
                 f"Updated: {repo_dict['updated_at']}\n" \
                 f"Description: {repo_dict['description']}\n"
        f.write(words)
        print(words)
