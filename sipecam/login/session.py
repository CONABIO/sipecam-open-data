import requests
from sipecam.login.user import CONFIG


def login_alfresco():
    """
    Login Alfresco with .env credentials through API KEY
    :returns session : requests.Session
    :raises Exception : when login failed
    """
    try:
        session = requests.Session()
        session.headers.update({'x-api-key': CONFIG.get("API_KEY")})

        return session
    except Exception as e:
        print("Login failed: ", e)
