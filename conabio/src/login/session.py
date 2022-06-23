import requests


def login_alfresco(api_key):
    """
    Creates a session in Alfresco

    Parameters
    ----------
    api_key : string
        Api key that can come from the .env credentials

    Return
    ------
    session : requests.Session
    """
    try:
        session = requests.Session()
        session.headers.update({'x-api-key': api_key})

        return session
    except Exception as e:
        print("Login failed: ", e)
