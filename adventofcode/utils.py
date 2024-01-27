from pathlib import Path
from requests import get
from urllib.parse import urlparse


def url_is_valid(u: str):
    try:
        result = urlparse(u)
        return all([result.scheme, result.netloc])
    except:
        return False


def read_text(src: Path | str) -> str:
    text = None
    src = Path(src)
    if src.exists():
        with open(src, "r") as io:
            text = io.read()
    elif url_is_valid(str(src)):
        resp = get(src)
        if resp.status_code == 200:
            text = resp.content
    return text
