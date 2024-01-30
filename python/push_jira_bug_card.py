import os
import requests
import json


#------------------------------------------------------------------------------
# get environment variables
#------------------------------------------------------------------------------

jira_api_key         = os.environ['JIRA_API_KEY'] 
jira_project_key     = os.environ['JIRA_PROJECT_KEY']
github_issue_type    = os.environ['GITHUB_ISSUE_TYPE']
github_issue_title   = os.environ['GITHUB_ISSUE_TITLE']
github_issue_body    = os.environ['GITHUB_ISSUE_BODY']

bug = "bug" in [x.lower() for x in github_issue_type]

if bug:
    print(f"""
    github_issue_type: {github_issue_type}
    github_issue_title: {github_issue_title}
    github_issue_body: {github_issue_body}
    """
    )

    jira_domain = 'cityofhope'  # without the https:// and .atlassian.net parts

    # API Endpoint
    url = f'https://{jira_domain}.atlassian.net/rest/api/3/issue/'

    # Headers
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Basic {jira_api_key}"
    }

    # Issue details
    payload = json.dumps({
        "fields": {
            "project": {
                "key": f"{jira_project_key}"
            },
            "summary": f"{github_issue_title}",
            "description": f"{github_issue_body}",
            "issuetype": {
                "name": "Task"
            }
        }
    })

    # Making the request
    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers
    )

    # Handling the response
    if response.status_code == 201:
        print(f"Successfully created a bug card. Response: {response.json()}")
    else:
        print(f"Failed to create a bug card. Status Code: {response.status_code}, Response: {response.text}")

