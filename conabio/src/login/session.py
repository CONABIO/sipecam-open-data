import requests

from conabio.src.login.user import CONFIG


def login_alfresco(config=CONFIG):
    """
    Login Alfresco with .env credentials

    Return
    ------
    session : requests.Session
    """
    try:
        session = requests.Session()
        session.headers.update({'x-api-key': config.get("API_KEY")})

        return session
    except Exception as e:
        print("Login failed: ", e)
