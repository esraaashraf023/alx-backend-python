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
     """TestIntegrationGithubOrgClient"""
    @classmethod
    def setUpClass(cls):
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            """get_payload"""
            return unittest.mock.Mock(**{'json.return_value':
                                         route_payload[url]})

        cls.get_patcher = unittest.mock.patch("requests.get",
                                              side_effect=get_payload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Tests the `public_repos` method."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Tests the `public_repos` method with a license."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
