import json
import os
from datetime import datetime



def read_operations(file_path):
    with open(file_path, encoding='utf-8') as file:
        content = file.read()
        operations = json.loads(content)
        return operations