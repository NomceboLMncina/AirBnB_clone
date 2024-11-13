#!/usr/bin/python3
"""
Initialize the models package.

This module creates a unique FileStorage instance for the application
and reloads any saved objects from storage.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
