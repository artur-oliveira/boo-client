import requests


def http_session() -> requests.Session:
    return requests.Session()
