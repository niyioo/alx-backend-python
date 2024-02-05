#!/usr/bin/env python3
"""
Module for testing client functions
"""


import unittest
from unittest.mock import patch
from parameterized import parameterized_class, parameterized
from client import GithubOrgClient  # Import your GithubOrgClient class

class TestGithubOrgClient(unittest.TestCase):
    """
    Test suite for GithubOrgClient
    """

    @parameterized_class("org_payload", "repos_payload", "expected_repos", "apache2_repos",
                         fixtures.get_fixtures())  # Import your fixtures module
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        """
        Integration test suite for GithubOrgClient
        """

        @classmethod
        def setUpClass(cls, org_payload, repos_payload, expected_repos, apache2_repos):
            """
            Setup method for the integration test class
            """
            cls.get_patcher = patch('requests.get')
            cls.mock_get = cls.get_patcher.start()

            # Configure side_effect for requests.get(url).json() based on fixtures
            cls.mock_get.side_effect = [
                org_payload,
                repos_payload,
                expected_repos,
                apache2_repos,
            ]

        @classmethod
        def tearDownClass(cls):
            """
            Teardown method for the integration test class
            """
            cls.get_patcher.stop()

        def test_public_repos(self):
            """
            Test GithubOrgClient.public_repos in an integration test
            """
            client = GithubOrgClient("example_org")
            repos = client.public_repos()

            # Assert that the result matches the expected_repos from fixtures
            self.assertEqual(repos, expected_repos)

        def test_public_repos_with_license(self):
            """
            Test GithubOrgClient.public_repos with license argument in an integration test
            """
            client = GithubOrgClient("example_org")
            repos = client.public_repos(license="apache-2.0")

            # Assert that the result matches the apache2_repos from fixtures
            self.assertEqual(repos, apache2_repos)


class TestGithubOrgClientUnitTests(unittest.TestCase):
    """
    Unit test suite for GithubOrgClient
    """

    @patch('requests.get')
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    def test_org(self, org_name, expected_payload, mock_get):
        """
        Test GithubOrgClient.org using @patch as a decorator and @parameterized.expand
        """
        mock_get.return_value.json.return_value = expected_payload
        client = GithubOrgClient(org_name)
        result = client.org()

        # Assert that get_json was called once with the expected argument
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

        # Assert that the result matches the expected_payload
        self.assertEqual(result, expected_payload)


    @patch.object(GithubOrgClient, 'org')
    def test_public_repos_url(self, mock_org):
        """
        Test GithubOrgClient._public_repos_url using @patch as a decorator
        """
        # Configure mock_org to return a known payload
        mock_org.return_value = {"repos": ["repo1", "repo2"]}

        client = GithubOrgClient("example_org")
        result = client._public_repos_url()

        # Assert that the result is as expected based on the mocked payload
        self.assertEqual(result, "https://api.github.com/orgs/example_org/repos")


    @patch('requests.get')
    @patch.object(GithubOrgClient, '_public_repos_url', return_value="mocked_url")
    def test_public_repos(self, mock_public_repos_url, mock_get):
        """
        Test GithubOrgClient.public_repos using @patch as a decorator
        """
        # Configure mock_get to return a known payload
        mock_get.return_value.json.return_value = {"repos": ["repo1", "repo2"]}

        client = GithubOrgClient("example_org")
        repos = client.public_repos()

        # Assert that get_json and _public_repos_url were called once
        mock_get.assert_called_once_with("mocked_url")
        mock_public_repos_url.assert_called_once()

        # Assert that the list of repos is what you expect from the chosen payload
        self.assertEqual(repos, ["repo1", "repo2"])


    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test GithubOrgClient.has_license using @parameterized.expand
        """
        client = GithubOrgClient("example_org")
        result = client.has_license(repo, license_key)

        # Assert that the result matches the expected returned value
        self.assertEqual(result, expected_result)
