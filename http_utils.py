import requests
from requests.adapters import HTTPAdapter


def http_session() -> requests.Session:
    session = requests.Session()
    adapter = HTTPAdapter(pool_connections=50, pool_maxsize=100)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session
