import requests

def get_issue_links(repo_url, milestone_number):
    url = f"{repo_url}/issues?milestone={milestone_number}&state=closed"
    response = requests.get(url)
    issues = response.json()
    
    issue_links = []
    for issue in issues:
        issue_links.append(issue['html_url'])
    
    return issue_links

# Replace these variables with the actual repository URL and milestone number
repository_url = "https://api.github.com/repos/hotosm/tasking-manager"
milestone_number = 64

issue_links = get_issue_links(repository_url, milestone_number)
for link in issue_links:
    print(link)
