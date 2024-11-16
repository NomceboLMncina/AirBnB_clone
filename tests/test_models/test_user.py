#!/usr/bin/python3
"""Unittest for User class"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up a User instance for testing."""
        self.user = User()

    def test_inheritance(self):
        """Test that User is a subclass of BaseModel."""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Test the default values of User attributes."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_attribute_assignment(self):
        """Test assigning values to User attributes."""
        self.user.email = "user@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        self.assertEqual(self.user.email, "user@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_to_dict_includes_user_attributes(self):
        """Test that the `to_dict` method includes User-specific attributes."""
        self.user.email = "user@example.com"
        self.user.password = "password123"
        user_dict = self.user.to_dict()

        self.assertIn("email", user_dict)
        self.assertIn("password", user_dict)
        self.assertIn("first_name", user_dict)
        self.assertIn("last_name", user_dict)
        self.assertEqual(user_dict["email"], "user@example.com")
        self.assertEqual(user_dict["password"], "password123")

    def test_string_representation(self):
        """Test the string representation of User."""
        user_str = str(self.user)
        self.assertIn("[User]", user_str)
        self.assertIn("id", user_str)
        self.assertIn("created_at", user_str)
        self.assertIn("updated_at", user_str)


if __name__ == "__main__":
    unittest.main()
