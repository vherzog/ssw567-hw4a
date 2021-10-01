# -*- coding: utf-8 -*-
# pylint: disable=W0311
# pylint: disable=broad-except
"""
Unit tests for the analyze_github python functions.

@author: vherzog
"""

import unittest
from analyze_github import check_input, check_message, analyze_github, count_commits, list_repos

GITHUB_USER_ID = "vherzog"
GITHUB_USER_ID_NOT_EXIST = "abc-do-re-me"
GITHUB_REPO = f"{GITHUB_USER_ID}/ssw567-hw4a"
GITHUB_REPO_NOT_EXIST = f"{GITHUB_USER_ID_NOT_EXIST}/fakerepo"
EXAMPLE_RESPONSE = [{'test key': 'test value'}]


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

        try:
            self.assertIsInstance(
                analyze_github(GITHUB_USER_ID),
                list,
                "No output expected."
            )
        except Exception:
            self.fail(
                f"check_input({GITHUB_USER_ID}) raised Exception unexpectedly!")

    def test_check_input_invalid(self):
        """Test check_input output when the GitHub user ID entered is invalid."""
        with self.assertRaises(Exception):
            check_input(123)

        with self.assertRaises(Exception):
            analyze_github(123)

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

        with self.assertRaises(Exception):
            analyze_github(GITHUB_USER_ID_NOT_EXIST)

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

    def test_count_commits_exist(self):
        """Test count_commits output when repo exists"""
        try:
            self.assertGreaterEqual(
                count_commits(GITHUB_REPO),
                1,
                "Should return a list with length >= 1"
            )
        except Exception:
            self.fail(
                f"count_commits({GITHUB_REPO}) raised Exception unexpectedly!")

    def test_count_commits_not_exist(self):
        """Test count_commits output when repo does not exist"""
        with self.assertRaises(Exception):
            count_commits(GITHUB_REPO_NOT_EXIST)

    def test_list_repos_exist(self):
        """Test list_repos output when user does exist"""
        try:
            self.assertIsInstance(
                list_repos(GITHUB_REPO),
                list,
                "Should return a list of repos"
            )
        except Exception:
            self.fail(
                f"count_commits({GITHUB_REPO}) raised Exception unexpectedly!")

    def test_list_repos_not_exist(self):
        """Test list_repos output when user does not exist"""
        with self.assertRaises(Exception):
            list_repos(GITHUB_USER_ID_NOT_EXIST)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
