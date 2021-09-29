# -*- coding: utf-8 -*-
"""
Unit tests for the analyze_github python functions.

@author: vherzog
"""

import unittest

from analyze_github import check_input, check_message, list_repos, count_commits, analyze_github

GITHUB_USER_ID = "vherzog"
EXAMPLE_RESPONSE = [{'test key': 'test value'}]


class TestAnalyzeGithub(unittest.TestCase):
    def test_check_input_valid(self):
        try:
            check_input(GITHUB_USER_ID)
        except ValueError:
            self.fail("check_input() raised ValueError unexpectedly!")

        try:
            analyze_github(GITHUB_USER_ID)
        except ValueError:
            self.fail("check_input() raised ValueError unexpectedly!")

    def test_check_input_invalid(self):
        with self.assertRaises(ValueError):
            check_input(123)

        with self.assertRaises(ValueError):
            analyze_github(123)

    def test_check_rate_limit_not_exceeded(self):
        self.assertEqual(check_message(
            EXAMPLE_RESPONSE),
            EXAMPLE_RESPONSE,
            "Response should be returned if rate limit is not exceeded"
        )

    def test_check_rate_limit_exceeded(self):
        with self.assertRaises(Exception):
            check_message(
                {"message": "API rate limit exceeded. Please wait to try again..."}
            )


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
