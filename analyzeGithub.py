# -*- coding: utf-8 -*-
"""
You should write a function that will
take as input a GitHub user ID.

The output from the function will be a
list of the names of the repositories that
the user has, along with the number of commits
that are in each of the listed repositories.


@author: vherzog

Questions:
- What type is the input? (string?)
- # of commits on the master/main branch? Or all branches?
- What should the format of the list output be? A list of dict? A list of tuples?
- What should the function do when hitting rate limiting?
- What error type/message should the function raise?
"""
import requests

def check_input(user_id):
    if not isinstance(user_id, str):
        raise ValueError("Please enter User ID as string")


def check_rate_limit(response):
    if isinstance(response, dict):
        if "message" in response and "API rate limit exceeded" in response["message"]:
            raise Exception(
                "ERROR: Github API Rate limit exceeded. Please wait before running again."
            )
    return response


def list_repos(user_id):
    repo_list = []
    query_url = f"https://api.github.com/users/{user_id}/repos"
    repos = check_rate_limit(requests.get(query_url).json())
    for repo in repos:
        repo_name = repo["full_name"]
        commit_count = count_commits(user_id, repo_name)
        repo_list.append({
            "repository_name": repo_name,
            "commit_count": commit_count
        })
    return repo_list


def count_commits(user_id, repo_name):
    query_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
    commits = requests.get(query_url).json()
    return len(commits)


def analyze_github(user_id):
    check_input(user_id)

    repos_list = list_repos(user_id)
    # print(repos_list)
    return repos_list


if __name__ == "__main__":
    analyze_github("vherzog")
