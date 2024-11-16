#!/usr/bin/python3
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_example(self):
        """Example test method"""
        model = BaseModel()
        self.assertIsNotNone(model)
