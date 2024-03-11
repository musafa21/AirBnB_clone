#!/usr/bin/python3

from models.engine.file_storage import FileStorage

"""
Initializes the FileStorage object and reloads the data.
"""
storage = FileStorage()
storage.reload()
