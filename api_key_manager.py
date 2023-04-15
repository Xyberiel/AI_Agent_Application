import os
import json

API_KEYS_FILE = "api_keys.json"

def save_api_keys(openai_api_key, google_api_key):
    api_keys = {
        "openai_api_key": openai_api_key,
        "google_api_key": google_api_key
    }

    with open(API_KEYS_FILE, "w") as f:
        json.dump(api_keys, f)

def load_api_keys():
    if not os.path.exists(API_KEYS_FILE):
        return None, None

    with open(API_KEYS_FILE, "r") as f:
        api_keys = json.load(f)

    return api_keys["openai_api_key"], api_keys["google_api_key"]

def validate_api_keys(openai_api_key, google_api_key):
    # Add your validation logic here, for example, by checking if they are not empty strings.
    if not openai_api_key or not google_api_key:
        return False

    # You can also add more specific validation checks for each API key.
    # ...

    return True

