import urllib.parse
from typing import Dict, List

import requests
from bs4 import BeautifulSoup, SoupStrainer

from .emoji import Emoji, categories


def category(category: str) -> List[str]:
    emoji_url = f"https://emojipedia.org/{category}"
    try:
        page = requests.get(emoji_url)
    except:
        print("Connection error")
        exit()
    try:
        soup = BeautifulSoup(page.content, 'lxml')
    except:
        print("Could not parse page content")
        exit()

    emojis: List[str]
    try:
        ul = soup.find('ul', class_="emoji-list")
        spans = ul.find_all('span', class_='emoji')
        emojis = [span.get_text() for span in spans]
    except:
        emojis = list()

    return emojis


def palette() -> dict:
    return dict([(c, category(c)) for c in categories])
