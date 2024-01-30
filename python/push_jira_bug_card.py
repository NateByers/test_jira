import os
import requests

jira_base_url        = os.environ['JIRA_BASE_URL']  
jira_user_email      = os.environ['JIRA_USER_EMAIL'] 
jira_organization_id = os.environ['JIRA_ORGANIZATION_ID'] 
jira_api_key         = os.environ['JIRA_API_KEY'] 
jira_project_key     = os.environ['JIRA_PROJECT_KEY']
github_issue_type    = os.environ['GITHUB_ISSUE_TYPE']
github_issue_title   = os.environ['GITHUB_ISSUE_TITLE']
github_issue_body    = os.environ['GITHUB_ISSUE_BODY']

print(f"""
Configuration:
jira_base_url: {jira_base_url}
jira_user_email: {jira_user_email}
jira_organization_id: {jira_organization_id}
jira_api_key: {jira_api_key}
github_issue_type: {github_issue_type}
github_issue_title: {github_issue_title}
github_issue_body: {github_issue_body}
"""
)
