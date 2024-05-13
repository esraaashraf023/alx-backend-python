#!/usr/bin/env python3
"""Unit testing for client module"""

import unittest
from typing import Dict
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Class for testing org method"""

    @parameterized.expand([
        'google',
        'abc'
        ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get: Mock):
        """Test org name"""
        payload: Dict[str, str] = {"org_name": org_name}

        mock_get.return_value = lambda: payload
        github_org_client = GithubOrgClient(org_name)
        self.assertEqual(github_org_client.org(), payload)
        mock_get.assert_called_once()

    def test_public_repos_url(self):
        """test public repos url"""
        with patch.object(GithubOrgClient, 'org',
                new_callable=PropertyMock) as mock_org:
            url = "https://google.com"
            mock_org.return_value = {"repos_url": url}

            github_org_client = GithubOrgClient("google")
            self.assertEqual(github_org_client._public_repos_url, url)

    @patch('client.get_json')
    def test_public_repos(self, get_mock):
        """test public repos method"""
        get_mock.return_value = [
                {"name": "repo1", "license": {"key": "MIT"}},
                {"name": "repo2", "license": {"key": "Apache"}}
                ]

        with patch.object(GithubOrgClient,
                '_public_repos_url',
                new_callable=PropertyMock) as repos_mock:
            repos_mock.return_value = "mocked_repos_url"

            github_client = GithubOrgClient("mocked_repos_url")
            self.assertEqual(github_client.public_repos(license="MIT"),
                    ["repo1"])
            get_mock.assert_called_once()
            repos_mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, license, result):
        """test has license"""
        github_client = GithubOrgClient("org_name")
        self.assertEqual(github_client.has_license(repo, license), result)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """"""

if __name__ == '__main__':
    unittest.main()
