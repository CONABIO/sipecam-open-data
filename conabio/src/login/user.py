from dotenv import dotenv_values


def set_environment(path=".env"):
    config = dotenv_values(path)
    return config


CONFIG = set_environment()
MAX_ITEMS = 5000
INCLUDE_FIELDS = ["properties", "path"]
