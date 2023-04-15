import os
import json
from pathlib import Path

MEMORY_DIR = "memory"
SHORT_TERM_FILE = "short_term_memory.json"
LONG_TERM_FILE = "long_term_memory.json"

class MemoryManager:
    def __init__(self):
        initialize_memory_directory()

    def read_short_term_memory(self):
        return read_json_file(SHORT_TERM_FILE)

    def write_short_term_memory(self, data):
        write_json_file(SHORT_TERM_FILE, data)

    def read_long_term_memory(self):
        return read_json_file(LONG_TERM_FILE)

    def write_long_term_memory(self, data):
        write_json_file(LONG_TERM_FILE, data)

def initialize_memory_directory():
    Path(MEMORY_DIR).mkdir(parents=True, exist_ok=True)

def read_json_file(filename):
    with open(os.path.join(MEMORY_DIR, filename), 'r') as file:
        return json.load(file)

def write_json_file(filename, data):
    with open(os.path.join(MEMORY_DIR, filename), 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    memory_manager = MemoryManager()
    memory_manager.write_short_term_memory({"test": "data"})
    print(memory_manager.read_short_term_memory())
