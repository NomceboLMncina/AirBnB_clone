#!/usr/bin/python3
"""This file defines the User class entries."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.
    Attributes:
        email (str): User email.
        password (str): User password.
        first_name (str): User first name.
        last_name (str): User last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
