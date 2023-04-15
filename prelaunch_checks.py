import os
import platform
from dotenv import load_dotenv, set_key

ENV_FILE = ".env"


def prelaunch_check(set_api_keys_callback=None):
    check_api_keys(set_api_keys_callback)
    check_environment()


def check_api_keys(set_api_keys_callback=None):
    load_dotenv(ENV_FILE)
    openai_api_key = os.getenv("OPENAI_API_KEY")
    google_api_key = os.getenv("GOOGLE_API_KEY")

    if not openai_api_key or not google_api_key:
        if set_api_keys_callback:
            openai_api_key, google_api_key = set_api_keys_callback()
        else:
            raise RuntimeError("Missing required API keys.")

        with open(ENV_FILE, "w") as env_file:
            set_key(ENV_FILE, "OPENAI_API_KEY", openai_api_key)
            set_key(ENV_FILE, "GOOGLE_API_KEY", google_api_key)

            print("API keys have been saved to the .env file.")

    return openai_api_key, google_api_key


def check_environment():
    os_name = platform.system()

    if os_name not in ["Windows", "Linux", "Darwin"]:
        raise RuntimeError(f"Unsupported operating system: {os_name}")

    # Perform additional environment checks if necessary


if __name__ == "__main__":
    prelaunch_check()
