#!/usr/bin/env python3
"""
Module for testing utils functions
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test suite for utils.access_nested_map
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test utils.access_nested_map with different inputs
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError, "Key 'a' not found in nested map"),
        ({"a": 1}, ("a", "b"), KeyError, "Key 'b' not found in nested map"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception, expected_message):
        """
        Test utils.access_nested_map raises KeyError with expected message
        """
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):
    """
    Test suite for utils.get_json
    """

    @patch('requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test utils.get_json with mocked HTTP calls
        """
        # Create a Mock object with a json method that returns test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Patch requests.get to return the mock_response
        with patch('requests.get', return_value=mock_response) as mock_get:
            result = get_json(test_url)

        # Assert that requests.get was called exactly once with the test_url
        mock_get.assert_called_once_with(test_url)

        # Assert that the output of get_json is equal to test_payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test suite for utils.memoize decorator
    """

    class TestClass:
        """
        Test class for memoization
        """

        def a_method(self):
            """
            A simple method
            """
            return 42

        @memoize
        def a_property(self):
            """
            A memoized property using memoize decorator
            """
            return self.a_method()

    def test_memoize(self):
        """
        Test the memoization behavior
        """
        # Create an instance of TestClass
        test_instance = self.TestClass()

        # Patch the a_method to ensure it won't be called during the test
        with patch.object(test_instance, 'a_method') as mock_a_method:
            # Call a_property twice
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()

        # Assert that a_method is only called once
        mock_a_method.assert_called_once()

        # Assert that the results are correct
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
