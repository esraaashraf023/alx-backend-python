#!/usr/bin/env python3

"""TestGithubOrgClient"""
import unittest
import unittest.mock
from parameterized import parameterized, parameterized_class  # type: ignore
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""

    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @unittest.mock.patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """test_org test"""
        expected_url = f"https://api.github.com/orgs/{org_name}"
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(expected_url)

    @unittest.mock.patch('client.GithubOrgClient.org',
                         new_callable=unittest.mock.PropertyMock)
    def test_public_repos_url(self, mock_org):
        """test_public_repos_url"""
        mock_org.return_value = {"repos_url":
                                 "https://api.github.com/orgs/testorg/repos"}
        client = GithubOrgClient("testorg")
        self.assertEqual(client._public_repos_url,
                         "https://api.github.com/orgs/testorg/repos")

    @unittest.mock.patch('client.get_json')
    @unittest.mock.patch('client.GithubOrgClient._public_repos_url',
                         new_callable=unittest.mock.PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """test_public_repos"""
        sample_payload = [
            {"name": "repo1", "license": {"key": "MIT"}},
        ]

        mock_public_repos_url.return_value = \
            "https://api.github.com/orgs/testorg/repos"
        mock_get_json.return_value = sample_payload

        client = GithubOrgClient("testorg")

        repos = client.public_repos(license="MIT")

        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/testorg/repos")
        mock_public_repos_url.assert_called_once()

        self.assertEqual(repos, ["repo1"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """test_has_license"""
        client = GithubOrgClient("testorg")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
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
        """Removes the class"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Tests method."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Tests"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
