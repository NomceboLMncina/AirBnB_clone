#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
import time
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up a BaseModel instance for testing."""
        self.base_model = BaseModel()

    def test_instance_creation(self):
        """Test if a BaseModel instance is created correctly."""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model.id, str)
        self.assertTrue(len(self.base_model.id), 36)  # Check UUID length
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertEqual(self.base_model.created_at, self.base_model.updated_at)

    def test_unique_ids(self):
        """Test that two BaseModel instances have unique IDs."""
        another_instance = BaseModel()
        self.assertNotEqual(self.base_model.id, another_instance.id)

    def test_save_method(self):
        """Test the save method updates the updated_at timestamp."""
        previous_updated_at = self.base_model.updated_at
        time.sleep(1)  # Ensure a time difference for testing
        self.base_model.save()
        self.assertGreater(self.base_model.updated_at, previous_updated_at)

    def test_to_dict(self):
        """Test that to_dict returns a correct dictionary representation."""
        base_dict = self.base_model.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertEqual(base_dict["id"], self.base_model.id)
        self.assertEqual(base_dict["created_at"], self.base_model.created_at.isoformat())
        self.assertEqual(base_dict["updated_at"], self.base_model.updated_at.isoformat())

    def test_to_dict_output(self):
        """Test that to_dict produces the correct keys and values."""
        base_dict = self.base_model.to_dict()
        expected_keys = {"id", "created_at", "updated_at", "__class__"}
        self.assertTrue(expected_keys.issubset(base_dict.keys()))

    def test_kwargs_initialization(self):
        """Test initialization of BaseModel with kwargs."""
        base_dict = self.base_model.to_dict()
        new_instance = BaseModel(**base_dict)
        self.assertEqual(new_instance.id, self.base_model.id)
        self.assertEqual(new_instance.created_at, self.base_model.created_at)
        self.assertEqual(new_instance.updated_at, self.base_model.updated_at)
        self.assertNotIn("__class__", new_instance.__dict__)

    def test_str_representation(self):
        """Test the string representation of the BaseModel instance."""
        string_representation = str(self.base_model)
        self.assertIn("[BaseModel]", string_representation)
        self.assertIn(f"({self.base_model.id})", string_representation)
        self.assertIn("created_at", string_representation)
        self.assertIn("updated_at", string_representation)


if __name__ == "__main__":
    unittest.main()
