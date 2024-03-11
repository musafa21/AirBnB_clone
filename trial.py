#!bin/bash/python3

import os
import shutil

# Define the file paths and their corresponding destinations
file_paths = [
    ("tests/", "AirBnB_clone"),
    ("models/base_model.py", "AirBnB_clone"),
    ("models/__init__.py", "AirBnB_clone"),
    ("models/base_model.py", "AirBnB_clone/tests/"),
    ("models/engine/file_storage.py", "AirBnB_clone"),
    ("models/engine/__init__.py", "AirBnB_clone"),
    ("models/__init__.py", "AirBnB_clone"),
    ("models/base_model.py", "AirBnB_clone/tests/"),
    ("console.py", "AirBnB_clone"),
    ("models/user.py", "AirBnB_clone"),
    ("models/engine/file_storage.py", "AirBnB_clone"),
    ("console.py", "AirBnB_clone/tests/"),
    ("models/state.py", "AirBnB_clone"),
    ("models/city.py", "AirBnB_clone"),
    ("models/amenity.py", "AirBnB_clone"),
    ("models/place.py", "AirBnB_clone"),
    ("models/review.py", "AirBnB_clone"),
    ("tests/", "AirBnB_clone")
]

# Iterate over the file paths and move the files to their destinations
for file_path, destination in file_paths:
    if not os.path.exists(destination):
        os.makedirs(destination)
    shutil.move(file_path, destination)