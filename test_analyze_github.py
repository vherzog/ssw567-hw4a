# -*- coding: utf-8 -*-
# pylint: disable=W0311
# pylint: disable=broad-except
"""
Unit tests for the analyze_github python functions.

@author: vherzog
"""

import unittest
from unittest.mock import patch, Mock
from analyze_github import check_input, check_message, analyze_github, count_commits, list_repos

GITHUB_USER_ID = "vherzog"
GITHUB_USER_ID_NOT_EXIST = "abc-do-re-me"
GITHUB_REPO = f"{GITHUB_USER_ID}/ssw567-hw4a"
GITHUB_REPO_NOT_EXIST = f"{GITHUB_USER_ID_NOT_EXIST}/fakerepo"
EXAMPLE_RESPONSE = [{'test key': 'test value'}]
COMMITS_RESPONSE_VALID = [
   {
      "sha":"f5b8fed3a266b23b2a7f10f7164c8899591ea50c",
      "node_id":"MDY6Q29tbWl0NDAxMTYwODczOmY1YjhmZWQzYTI2NmIyM2IyYTdmMTBmNzE2NGM4ODk5NTkxZWE1MGM=",
      "commit":{
         "author":{
            "name":"Veronica Herzog",
            "email":"v.herzog92@gmail.com",
            "date":"2021-09-07T01:09:37Z"
         },
         "committer":{
            "name":"GitHub",
            "email":"noreply@github.com",
            "date":"2021-09-07T01:09:37Z"
         },
         "message":"Update README.md",
         "tree":{
            "sha":"59b912d957696105a062e809ec514e14a743bdca",
            "url":"https://api.github.com/repos/vherzog/ssw567/git/trees/59b912d957696105a062e809ec514e14a743bdca"
         },
         "url":"https://api.github.com/repos/vherzog/ssw567/git/commits/f5b8fed3a266b23b2a7f10f7164c8899591ea50c",
         "comment_count":0,
         "verification":{
            "verified":True,
            "reason":"valid",
            "signature":"-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJhNrvRCRBK7hj4Ov3rIwAAyGIIABxKycLCjG7AuSzeNhjcDTDz\nbhuElvUPRzAYuSzGz+yh0g4E7jB5LnAjMdzXEfvSSY0G1a6Sp7gnYeomjLmPGLvE\nTtw5R5i+azBH4jWJSBGbHKu8A8A1bKH914+r2s5ZuAqhoy/jsjEcnlyrdGpHst54\n9sEW/WFfwsOACvJ3M/YlyQgbdUkIF3+gCVBaNBxnclIIKH6y/3yZh5QRV8ZvnI48\nN51JtIzqL8ka+DbGLmTy07Uq4SIl840/qFMEHcu9GW7d5jGJZ8qKcgGwxfnoTyri\nrSOraz+ZrzEx5VBxdFONxKktD0bvRJmAmkIX2QZOqE1YBWV2sfTG5r/rdM27rII=\n=qmum\n-----END PGP SIGNATURE-----\n",
            "payload":"tree 59b912d957696105a062e809ec514e14a743bdca\nparent 62efe7faa1f90d3266d2d23cab637201e8d7ed9d\nauthor Veronica Herzog <v.herzog92@gmail.com> 1630976977 -0400\ncommitter GitHub <noreply@github.com> 1630976977 -0400\n\nUpdate README.md"
         }
      },
      "url":"https://api.github.com/repos/vherzog/ssw567/commits/f5b8fed3a266b23b2a7f10f7164c8899591ea50c",
      "html_url":"https://github.com/vherzog/ssw567/commit/f5b8fed3a266b23b2a7f10f7164c8899591ea50c",
      "comments_url":"https://api.github.com/repos/vherzog/ssw567/commits/f5b8fed3a266b23b2a7f10f7164c8899591ea50c/comments",
      "author":{
         "login":"vherzog",
         "id":10634929,
         "node_id":"MDQ6VXNlcjEwNjM0OTI5",
         "avatar_url":"https://avatars.githubusercontent.com/u/10634929?v=4",
         "gravatar_id":"",
         "url":"https://api.github.com/users/vherzog",
         "html_url":"https://github.com/vherzog",
         "followers_url":"https://api.github.com/users/vherzog/followers",
         "following_url":"https://api.github.com/users/vherzog/following{/other_user}",
         "gists_url":"https://api.github.com/users/vherzog/gists{/gist_id}",
         "starred_url":"https://api.github.com/users/vherzog/starred{/owner}{/repo}",
         "subscriptions_url":"https://api.github.com/users/vherzog/subscriptions",
         "organizations_url":"https://api.github.com/users/vherzog/orgs",
         "repos_url":"https://api.github.com/users/vherzog/repos",
         "events_url":"https://api.github.com/users/vherzog/events{/privacy}",
         "received_events_url":"https://api.github.com/users/vherzog/received_events",
         "type":"User",
         "site_admin":False
      },
      "committer":{
         "login":"web-flow",
         "id":19864447,
         "node_id":"MDQ6VXNlcjE5ODY0NDQ3",
         "avatar_url":"https://avatars.githubusercontent.com/u/19864447?v=4",
         "gravatar_id":"",
         "url":"https://api.github.com/users/web-flow",
         "html_url":"https://github.com/web-flow",
         "followers_url":"https://api.github.com/users/web-flow/followers",
         "following_url":"https://api.github.com/users/web-flow/following{/other_user}",
         "gists_url":"https://api.github.com/users/web-flow/gists{/gist_id}",
         "starred_url":"https://api.github.com/users/web-flow/starred{/owner}{/repo}",
         "subscriptions_url":"https://api.github.com/users/web-flow/subscriptions",
         "organizations_url":"https://api.github.com/users/web-flow/orgs",
         "repos_url":"https://api.github.com/users/web-flow/repos",
         "events_url":"https://api.github.com/users/web-flow/events{/privacy}",
         "received_events_url":"https://api.github.com/users/web-flow/received_events",
         "type":"User",
         "site_admin":False
      },
      "parents":[
         {
            "sha":"62efe7faa1f90d3266d2d23cab637201e8d7ed9d",
            "url":"https://api.github.com/repos/vherzog/ssw567/commits/62efe7faa1f90d3266d2d23cab637201e8d7ed9d",
            "html_url":"https://github.com/vherzog/ssw567/commit/62efe7faa1f90d3266d2d23cab637201e8d7ed9d"
         }
      ]
   },
   {
      "sha":"62efe7faa1f90d3266d2d23cab637201e8d7ed9d",
      "node_id":"MDY6Q29tbWl0NDAxMTYwODczOjYyZWZlN2ZhYTFmOTBkMzI2NmQyZDIzY2FiNjM3MjAxZThkN2VkOWQ=",
      "commit":{
         "author":{
            "name":"vherzog",
            "email":"v.herzog92@gmail.com",
            "date":"2021-08-30T00:13:57Z"
         },
         "committer":{
            "name":"vherzog",
            "email":"v.herzog92@gmail.com",
            "date":"2021-08-30T00:13:57Z"
         },
         "message":"add travis ci status",
         "tree":{
            "sha":"5aa6ccfe35c56096bc7d6f930a9abd3739459566",
            "url":"https://api.github.com/repos/vherzog/ssw567/git/trees/5aa6ccfe35c56096bc7d6f930a9abd3739459566"
         },
         "url":"https://api.github.com/repos/vherzog/ssw567/git/commits/62efe7faa1f90d3266d2d23cab637201e8d7ed9d",
         "comment_count":0,
         "verification":{
            "verified":False,
            "reason":"unsigned",
            "signature":"null",
            "payload":"null"
         }
      },
      "url":"https://api.github.com/repos/vherzog/ssw567/commits/62efe7faa1f90d3266d2d23cab637201e8d7ed9d",
      "html_url":"https://github.com/vherzog/ssw567/commit/62efe7faa1f90d3266d2d23cab637201e8d7ed9d",
      "comments_url":"https://api.github.com/repos/vherzog/ssw567/commits/62efe7faa1f90d3266d2d23cab637201e8d7ed9d/comments",
      "author":{
         "login":"vherzog",
         "id":10634929,
         "node_id":"MDQ6VXNlcjEwNjM0OTI5",
         "avatar_url":"https://avatars.githubusercontent.com/u/10634929?v=4",
         "gravatar_id":"",
         "url":"https://api.github.com/users/vherzog",
         "html_url":"https://github.com/vherzog",
         "followers_url":"https://api.github.com/users/vherzog/followers",
         "following_url":"https://api.github.com/users/vherzog/following{/other_user}",
         "gists_url":"https://api.github.com/users/vherzog/gists{/gist_id}",
         "starred_url":"https://api.github.com/users/vherzog/starred{/owner}{/repo}",
         "subscriptions_url":"https://api.github.com/users/vherzog/subscriptions",
         "organizations_url":"https://api.github.com/users/vherzog/orgs",
         "repos_url":"https://api.github.com/users/vherzog/repos",
         "events_url":"https://api.github.com/users/vherzog/events{/privacy}",
         "received_events_url":"https://api.github.com/users/vherzog/received_events",
         "type":"User",
         "site_admin":False
      },
      "committer":{
         "login":"vherzog",
         "id":10634929,
         "node_id":"MDQ6VXNlcjEwNjM0OTI5",
         "avatar_url":"https://avatars.githubusercontent.com/u/10634929?v=4",
         "gravatar_id":"",
         "url":"https://api.github.com/users/vherzog",
         "html_url":"https://github.com/vherzog",
         "followers_url":"https://api.github.com/users/vherzog/followers",
         "following_url":"https://api.github.com/users/vherzog/following{/other_user}",
         "gists_url":"https://api.github.com/users/vherzog/gists{/gist_id}",
         "starred_url":"https://api.github.com/users/vherzog/starred{/owner}{/repo}",
         "subscriptions_url":"https://api.github.com/users/vherzog/subscriptions",
         "organizations_url":"https://api.github.com/users/vherzog/orgs",
         "repos_url":"https://api.github.com/users/vherzog/repos",
         "events_url":"https://api.github.com/users/vherzog/events{/privacy}",
         "received_events_url":"https://api.github.com/users/vherzog/received_events",
         "type":"User",
         "site_admin":False
      },
      "parents":[
         {
            "sha":"927f3aa139b450be5a2c925e0f7601100dc35748",
            "url":"https://api.github.com/repos/vherzog/ssw567/commits/927f3aa139b450be5a2c925e0f7601100dc35748",
            "html_url":"https://github.com/vherzog/ssw567/commit/927f3aa139b450be5a2c925e0f7601100dc35748"
         }
      ]
   }
]
COMMITS_RESPONSE_INVALID = {
  "message": "Not Found",
  "documentation_url": "https://docs.github.com/rest/reference/repos#list-commits"
}
REPOS_RESPONSE_VALID = [
  {
    "id": 401160873,
    "node_id": "MDEwOlJlcG9zaXRvcnk0MDExNjA4NzM=",
    "name": "ssw567",
    "full_name": "vherzog/ssw567",
    "private": False,
    "owner": {
      "login": "vherzog",
      "id": 10634929,
      "node_id": "MDQ6VXNlcjEwNjM0OTI5",
      "avatar_url": "https://avatars.githubusercontent.com/u/10634929?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/vherzog",
      "html_url": "https://github.com/vherzog",
      "followers_url": "https://api.github.com/users/vherzog/followers",
      "following_url": "https://api.github.com/users/vherzog/following{/other_user}",
      "gists_url": "https://api.github.com/users/vherzog/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/vherzog/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/vherzog/subscriptions",
      "organizations_url": "https://api.github.com/users/vherzog/orgs",
      "repos_url": "https://api.github.com/users/vherzog/repos",
      "events_url": "https://api.github.com/users/vherzog/events{/privacy}",
      "received_events_url": "https://api.github.com/users/vherzog/received_events",
      "type": "User",
      "site_admin": False
    },
    "html_url": "https://github.com/vherzog/ssw567",
    "description": "null",
    "fork": False,
    "url": "https://api.github.com/repos/vherzog/ssw567",
    "forks_url": "https://api.github.com/repos/vherzog/ssw567/forks",
    "keys_url": "https://api.github.com/repos/vherzog/ssw567/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/vherzog/ssw567/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/vherzog/ssw567/teams",
    "hooks_url": "https://api.github.com/repos/vherzog/ssw567/hooks",
    "issue_events_url": "https://api.github.com/repos/vherzog/ssw567/issues/events{/number}",
    "events_url": "https://api.github.com/repos/vherzog/ssw567/events",
    "assignees_url": "https://api.github.com/repos/vherzog/ssw567/assignees{/user}",
    "branches_url": "https://api.github.com/repos/vherzog/ssw567/branches{/branch}",
    "tags_url": "https://api.github.com/repos/vherzog/ssw567/tags",
    "blobs_url": "https://api.github.com/repos/vherzog/ssw567/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/vherzog/ssw567/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/vherzog/ssw567/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/vherzog/ssw567/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/vherzog/ssw567/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/vherzog/ssw567/languages",
    "stargazers_url": "https://api.github.com/repos/vherzog/ssw567/stargazers",
    "contributors_url": "https://api.github.com/repos/vherzog/ssw567/contributors",
    "subscribers_url": "https://api.github.com/repos/vherzog/ssw567/subscribers",
    "subscription_url": "https://api.github.com/repos/vherzog/ssw567/subscription",
    "commits_url": "https://api.github.com/repos/vherzog/ssw567/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/vherzog/ssw567/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/vherzog/ssw567/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/vherzog/ssw567/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/vherzog/ssw567/contents/{+path}",
    "compare_url": "https://api.github.com/repos/vherzog/ssw567/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/vherzog/ssw567/merges",
    "archive_url": "https://api.github.com/repos/vherzog/ssw567/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/vherzog/ssw567/downloads",
    "issues_url": "https://api.github.com/repos/vherzog/ssw567/issues{/number}",
    "pulls_url": "https://api.github.com/repos/vherzog/ssw567/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/vherzog/ssw567/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/vherzog/ssw567/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/vherzog/ssw567/labels{/name}",
    "releases_url": "https://api.github.com/repos/vherzog/ssw567/releases{/id}",
    "deployments_url": "https://api.github.com/repos/vherzog/ssw567/deployments",
    "created_at": "2021-08-29T23:10:29Z",
    "updated_at": "2021-09-07T01:09:40Z",
    "pushed_at": "2021-09-07T01:09:37Z",
    "git_url": "git://github.com/vherzog/ssw567.git",
    "ssh_url": "git@github.com:vherzog/ssw567.git",
    "clone_url": "https://github.com/vherzog/ssw567.git",
    "svn_url": "https://github.com/vherzog/ssw567",
    "homepage": "null",
    "size": 5,
    "stargazers_count": 0,
    "watchers_count": 0,
    "language": "Python",
    "has_issues": True,
    "has_projects": True,
    "has_downloads": True,
    "has_wiki": True,
    "has_pages": False,
    "forks_count": 0,
    "mirror_url": "null",
    "archived": False,
    "disabled": False,
    "open_issues_count": 0,
    "license": "null",
    "allow_forking": True,
    "is_template": False,
    "topics": [

    ],
    "visibility": "public",
    "forks": 0,
    "open_issues": 0,
    "watchers": 0,
    "default_branch": "main"
  },
  {
    "id": 405427678,
    "node_id": "MDEwOlJlcG9zaXRvcnk0MDU0Mjc2Nzg=",
    "name": "ssw567-hw1",
    "full_name": "vherzog/ssw567-hw1",
    "private": False,
    "owner": {
      "login": "vherzog",
      "id": 10634929,
      "node_id": "MDQ6VXNlcjEwNjM0OTI5",
      "avatar_url": "https://avatars.githubusercontent.com/u/10634929?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/vherzog",
      "html_url": "https://github.com/vherzog",
      "followers_url": "https://api.github.com/users/vherzog/followers",
      "following_url": "https://api.github.com/users/vherzog/following{/other_user}",
      "gists_url": "https://api.github.com/users/vherzog/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/vherzog/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/vherzog/subscriptions",
      "organizations_url": "https://api.github.com/users/vherzog/orgs",
      "repos_url": "https://api.github.com/users/vherzog/repos",
      "events_url": "https://api.github.com/users/vherzog/events{/privacy}",
      "received_events_url": "https://api.github.com/users/vherzog/received_events",
      "type": "User",
      "site_admin": False
    },
    "html_url": "https://github.com/vherzog/ssw567-hw1",
    "description": "SSW567 Homework 1",
    "fork": False,
    "url": "https://api.github.com/repos/vherzog/ssw567-hw1",
    "forks_url": "https://api.github.com/repos/vherzog/ssw567-hw1/forks",
    "keys_url": "https://api.github.com/repos/vherzog/ssw567-hw1/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/vherzog/ssw567-hw1/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/vherzog/ssw567-hw1/teams",
    "hooks_url": "https://api.github.com/repos/vherzog/ssw567-hw1/hooks",
    "issue_events_url": "https://api.github.com/repos/vherzog/ssw567-hw1/issues/events{/number}",
    "events_url": "https://api.github.com/repos/vherzog/ssw567-hw1/events",
    "assignees_url": "https://api.github.com/repos/vherzog/ssw567-hw1/assignees{/user}",
    "branches_url": "https://api.github.com/repos/vherzog/ssw567-hw1/branches{/branch}",
    "tags_url": "https://api.github.com/repos/vherzog/ssw567-hw1/tags",
    "blobs_url": "https://api.github.com/repos/vherzog/ssw567-hw1/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/vherzog/ssw567-hw1/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/vherzog/ssw567-hw1/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/vherzog/ssw567-hw1/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/vherzog/ssw567-hw1/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/vherzog/ssw567-hw1/languages",
    "stargazers_url": "https://api.github.com/repos/vherzog/ssw567-hw1/stargazers",
    "contributors_url": "https://api.github.com/repos/vherzog/ssw567-hw1/contributors",
    "subscribers_url": "https://api.github.com/repos/vherzog/ssw567-hw1/subscribers",
    "subscription_url": "https://api.github.com/repos/vherzog/ssw567-hw1/subscription",
    "commits_url": "https://api.github.com/repos/vherzog/ssw567-hw1/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/vherzog/ssw567-hw1/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/vherzog/ssw567-hw1/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/vherzog/ssw567-hw1/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/vherzog/ssw567-hw1/contents/{+path}",
    "compare_url": "https://api.github.com/repos/vherzog/ssw567-hw1/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/vherzog/ssw567-hw1/merges",
    "archive_url": "https://api.github.com/repos/vherzog/ssw567-hw1/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/vherzog/ssw567-hw1/downloads",
    "issues_url": "https://api.github.com/repos/vherzog/ssw567-hw1/issues{/number}",
    "pulls_url": "https://api.github.com/repos/vherzog/ssw567-hw1/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/vherzog/ssw567-hw1/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/vherzog/ssw567-hw1/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/vherzog/ssw567-hw1/labels{/name}",
    "releases_url": "https://api.github.com/repos/vherzog/ssw567-hw1/releases{/id}",
    "deployments_url": "https://api.github.com/repos/vherzog/ssw567-hw1/deployments",
    "created_at": "2021-09-11T16:27:27Z",
    "updated_at": "2021-09-11T20:36:22Z",
    "pushed_at": "2021-09-11T20:36:19Z",
    "git_url": "git://github.com/vherzog/ssw567-hw1.git",
    "ssh_url": "git@github.com:vherzog/ssw567-hw1.git",
    "clone_url": "https://github.com/vherzog/ssw567-hw1.git",
    "svn_url": "https://github.com/vherzog/ssw567-hw1",
    "homepage": "null",
    "size": 19,
    "stargazers_count": 0,
    "watchers_count": 0,
    "language": "Python",
    "has_issues": True,
    "has_projects": True,
    "has_downloads": True,
    "has_wiki": True,
    "has_pages": False,
    "forks_count": 0,
    "mirror_url": "null",
    "archived": False,
    "disabled": False,
    "open_issues_count": 0,
    "license": "null",
    "allow_forking": True,
    "is_template": False,
    "topics": [

    ],
    "visibility": "public",
    "forks": 0,
    "open_issues": 0,
    "watchers": 0,
    "default_branch": "main"
  },
  {
    "id": 406065032,
    "node_id": "MDEwOlJlcG9zaXRvcnk0MDYwNjUwMzI=",
    "name": "ssw567-hw2",
    "full_name": "vherzog/ssw567-hw2",
    "private": False,
    "owner": {
      "login": "vherzog",
      "id": 10634929,
      "node_id": "MDQ6VXNlcjEwNjM0OTI5",
      "avatar_url": "https://avatars.githubusercontent.com/u/10634929?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/vherzog",
      "html_url": "https://github.com/vherzog",
      "followers_url": "https://api.github.com/users/vherzog/followers",
      "following_url": "https://api.github.com/users/vherzog/following{/other_user}",
      "gists_url": "https://api.github.com/users/vherzog/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/vherzog/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/vherzog/subscriptions",
      "organizations_url": "https://api.github.com/users/vherzog/orgs",
      "repos_url": "https://api.github.com/users/vherzog/repos",
      "events_url": "https://api.github.com/users/vherzog/events{/privacy}",
      "received_events_url": "https://api.github.com/users/vherzog/received_events",
      "type": "User",
      "site_admin": False
    },
    "html_url": "https://github.com/vherzog/ssw567-hw2",
    "description": "SSW567 Homework 2",
    "fork": False,
    "url": "https://api.github.com/repos/vherzog/ssw567-hw2",
    "forks_url": "https://api.github.com/repos/vherzog/ssw567-hw2/forks",
    "keys_url": "https://api.github.com/repos/vherzog/ssw567-hw2/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/vherzog/ssw567-hw2/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/vherzog/ssw567-hw2/teams",
    "hooks_url": "https://api.github.com/repos/vherzog/ssw567-hw2/hooks",
    "issue_events_url": "https://api.github.com/repos/vherzog/ssw567-hw2/issues/events{/number}",
    "events_url": "https://api.github.com/repos/vherzog/ssw567-hw2/events",
    "assignees_url": "https://api.github.com/repos/vherzog/ssw567-hw2/assignees{/user}",
    "branches_url": "https://api.github.com/repos/vherzog/ssw567-hw2/branches{/branch}",
    "tags_url": "https://api.github.com/repos/vherzog/ssw567-hw2/tags",
    "blobs_url": "https://api.github.com/repos/vherzog/ssw567-hw2/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/vherzog/ssw567-hw2/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/vherzog/ssw567-hw2/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/vherzog/ssw567-hw2/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/vherzog/ssw567-hw2/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/vherzog/ssw567-hw2/languages",
    "stargazers_url": "https://api.github.com/repos/vherzog/ssw567-hw2/stargazers",
    "contributors_url": "https://api.github.com/repos/vherzog/ssw567-hw2/contributors",
    "subscribers_url": "https://api.github.com/repos/vherzog/ssw567-hw2/subscribers",
    "subscription_url": "https://api.github.com/repos/vherzog/ssw567-hw2/subscription",
    "commits_url": "https://api.github.com/repos/vherzog/ssw567-hw2/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/vherzog/ssw567-hw2/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/vherzog/ssw567-hw2/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/vherzog/ssw567-hw2/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/vherzog/ssw567-hw2/contents/{+path}",
    "compare_url": "https://api.github.com/repos/vherzog/ssw567-hw2/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/vherzog/ssw567-hw2/merges",
    "archive_url": "https://api.github.com/repos/vherzog/ssw567-hw2/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/vherzog/ssw567-hw2/downloads",
    "issues_url": "https://api.github.com/repos/vherzog/ssw567-hw2/issues{/number}",
    "pulls_url": "https://api.github.com/repos/vherzog/ssw567-hw2/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/vherzog/ssw567-hw2/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/vherzog/ssw567-hw2/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/vherzog/ssw567-hw2/labels{/name}",
    "releases_url": "https://api.github.com/repos/vherzog/ssw567-hw2/releases{/id}",
    "deployments_url": "https://api.github.com/repos/vherzog/ssw567-hw2/deployments",
    "created_at": "2021-09-13T17:20:00Z",
    "updated_at": "2021-10-09T20:27:51Z",
    "pushed_at": "2021-10-09T20:27:48Z",
    "git_url": "git://github.com/vherzog/ssw567-hw2.git",
    "ssh_url": "git@github.com:vherzog/ssw567-hw2.git",
    "clone_url": "https://github.com/vherzog/ssw567-hw2.git",
    "svn_url": "https://github.com/vherzog/ssw567-hw2",
    "homepage": "null",
    "size": 96,
    "stargazers_count": 0,
    "watchers_count": 0,
    "language": "Python",
    "has_issues": True,
    "has_projects": True,
    "has_downloads": True,
    "has_wiki": True,
    "has_pages": False,
    "forks_count": 0,
    "mirror_url": "null",
    "archived": False,
    "disabled": False,
    "open_issues_count": 0,
    "license": "null",
    "allow_forking": True,
    "is_template": False,
    "topics": [

    ],
    "visibility": "public",
    "forks": 0,
    "open_issues": 0,
    "watchers": 0,
    "default_branch": "main"
  }
]
REPOS_RESPONSE_INVALID = {
  "message": "Not Found",
  "documentation_url": "https://docs.github.com/rest/reference/repos#list-repositories-for-a-user"
}

class TestAnalyzeGithub(unittest.TestCase):
    """TestCase unittest class to test analyze_github functionality"""

    def test_check_input_valid_exist(self):
        """Test check_input output when GitHub user ID entered is valid and exists."""
        try:
            self.assertEqual(
                check_input(GITHUB_USER_ID),
                None,
                "No output expected."
            )
        except Exception:
            self.fail(
                f"check_input({GITHUB_USER_ID}) raised Exception unexpectedly!")

        # try:
        #     self.assertIsInstance(
        #         analyze_github(GITHUB_USER_ID),
        #         list,
        #         "No output expected."
        #     )
        # except Exception:
        #     self.fail(
        #         f"check_input({GITHUB_USER_ID}) raised Exception unexpectedly!")

    def test_check_input_invalid(self):
        """Test check_input output when the GitHub user ID entered is invalid."""
        with self.assertRaises(Exception):
            check_input(123)

        # with self.assertRaises(Exception):
        #     analyze_github(123)

    def test_check_input_valid_not_exist(self):
        """Test check_input output when the GitHub user ID entered
            is valid but does not exist."""
        try:
            self.assertEqual(
                check_input(GITHUB_USER_ID_NOT_EXIST),
                None,
                "No output expected."
            )
        except Exception:
            self.fail(
                f"check_input({GITHUB_USER_ID_NOT_EXIST}) raised Exception unexpectedly!")

        # with self.assertRaises(Exception):
        #     analyze_github(GITHUB_USER_ID_NOT_EXIST)

    def test_check_message_valid(self):
        """Test check_message output when API request response is successful."""
        try:
            self.assertEqual(
                check_message(EXAMPLE_RESPONSE),
                EXAMPLE_RESPONSE,
                "Response should be returned as is."
            )
        except Exception:
            self.fail(
                f"check_message({EXAMPLE_RESPONSE}) raised Exception unexpectedly!")

    def test_check_message_rate_limit(self):
        """Test check_message output when hitting GitHub API rate limiting."""
        with self.assertRaises(Exception):
            check_message({"message": "API rate limit exceeded...."})

    def test_check_message_not_found(self):
        """Test check_message output when API request result is not found."""
        with self.assertRaises(Exception):
            check_message({
                "message": "Not Found."})

    @patch('analyze_github.requests.get')
    def test_count_commits_exist(self, mock_get):
        """Test count_commits output when repo exists"""
        # Configure the mock to return a response with a `json()` method.
        mock_get.return_value.json.return_value = COMMITS_RESPONSE_VALID
        try:
            self.assertGreaterEqual(
                count_commits(GITHUB_REPO),
                1,
                "Should return a list with length >= 1"
            )
        except Exception:
            self.fail(
                f"count_commits({GITHUB_REPO}) raised Exception unexpectedly!")

    @patch('analyze_github.requests.get')
    def test_count_commits_not_exist(self, mock_get):
        """Test count_commits output when repo does not exist"""
        # Configure the mock to return a response with a `json()` method.
        mock_get.return_value.json.return_value = COMMITS_RESPONSE_INVALID
        with self.assertRaises(Exception):
            count_commits(GITHUB_REPO_NOT_EXIST)

    @patch('analyze_github.requests.get')
    def test_list_repos_exist(self, mock_get):
        """Test list_repos output when user does exist"""
        # Configure the mock to return a response with a `json()` method.
        mock_get.return_value.json.return_value = REPOS_RESPONSE_VALID
        try:
            self.assertIsInstance(
                list_repos(GITHUB_USER_ID),
                list,
                "Should return a list of repos"
            )
        except Exception:
            self.fail(
                f"count_commits({GITHUB_USER_ID}) raised Exception unexpectedly!")

    @patch('analyze_github.requests.get')
    def test_list_repos_not_exist(self, mock_get):
        """Test list_repos output when user does not exist"""
        # Configure the mock to return a response with a `json()` method.
        mock_get.return_value.json.return_value = REPOS_RESPONSE_INVALID
        with self.assertRaises(Exception):
            list_repos(GITHUB_USER_ID_NOT_EXIST)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
