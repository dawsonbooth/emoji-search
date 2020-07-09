import urllib.parse
from typing import Dict, List

import requests
from bs4 import BeautifulSoup, SoupStrainer

from .emoji import Emoji, categories


def category(category: str) -> List[str]:
    emoji_url = f"https://emojipedia.org/{category}"

    page = requests.get(emoji_url)
    soup = BeautifulSoup(page.content, 'lxml')

    emojis: List[str]
    try:
        ul = soup.find('ul', class_="emoji-list")
        spans = ul.find_all('span', class_='emoji')
        emojis = [span.get_text() for span in spans]
    except:
        emojis = list()

    return emojis


def all() -> dict:
    return dict([(c, category(c)) for c in categories])


def search(emoji: str) -> dict:
    emoji_url = f"https://emojipedia.org/{urllib.parse.quote(emoji)}"

    page = requests.get(emoji_url)
    soup = BeautifulSoup(page.content, 'lxml')

    # Name
    name: str
    try:
        name = soup.find('article').find(
            'h1').get_text().replace(f"{emoji} ", "")
    except:
        name = ""

    # Description
    description: str
    try:
        section_desc = soup.find('section', class_="description")
        description = "\n".join(p.get_text()
                                for p in section_desc.find_all('p'))
    except:
        description = ""

    # Aliases
    aliases: List[str]
    try:
        section_aliases = soup.find('section', class_="aliases")
        aliases = [li.get_text().replace(f"{emoji} ", "")
                   for li in section_aliases.find('ul').find_all('li')]
    except:
        aliases = list()

    # Apple Name
    apple_name: str
    try:
        section_applenames = soup.find('section', class_="applenames")
        apple_name = section_applenames.find(
            'p').get_text().replace(f"{emoji} ", "")
    except:
        apple_name = ""

    # Unicode Name
    unicode_name: str
    try:
        section_unicodenames = soup.find('section', class_="unicodename")
        unicode_name = section_unicodenames.find(
            'p').get_text().replace(f"{emoji} ", "")
    except:
        unicode_name = ""

    # Vendors
    vendors: Dict[str, List[str]]
    try:
        section_vendor_list = soup.find('section', class_="vendor-list")
        vendors = dict()
        for li_vendor in section_vendor_list.find('ul').find_all('li', recursive=False):
            vendor_name = li_vendor.find('div').find(
                'div').find('h2').get_text()
            vendor_versions = [p.get_text() for p in li_vendor.find_all(
                'p', class_='version-name')]
            vendors[vendor_name] = vendor_versions
    except:
        vendors = dict()

    emoji_info = {
        'emoji': emoji,
        'description': description,
        'name': name,
        'aliases': aliases,
        'apple_name': apple_name,
        'unicode_name': unicode_name,
        'vendors': vendors
    }

    return Emoji(**emoji_info)
