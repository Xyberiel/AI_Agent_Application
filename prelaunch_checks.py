import os
import platform
from dotenv import load_dotenv, set_key
from api_key_manager import load_api_keys, validate_api_keys

ENV_FILE = ".env"


def prelaunch_check(set_api_keys_callback=None):
    check_api_keys(set_api_keys_callback)
    check_environment()


def check_api_keys(set_api_keys_callback=None):
    openai_api_key, google_api_key = load_api_keys()
    if not validate_api_keys(openai_api_key, google_api_key):
        if set_api_keys_callback is not None:
            set_api_keys_callback()
        else:
            raise RuntimeError("Missing required API keys.")
    return openai_api_key, google_api_key


def check_environment():
    os_name = platform.system()

    if os_name not in ["Windows", "Linux", "Darwin"]:
        raise RuntimeError(f"Unsupported operating system: {os_name}")

    # Perform additional environment checks if necessary


if __name__ == "__main__":
    prelaunch_check()
