import urllib.parse
from typing import Dict, List

import requests
from bs4 import BeautifulSoup

from .emoji import Emoji, categories


def category(category: str) -> List[str]:
    """Get list of emojis in the given category"""

    emoji_url = f"https://emojipedia.org/{category}"

    page = requests.get(emoji_url)
    soup = BeautifulSoup(page.content, 'lxml')

    symbols: List[str]
    try:
        ul = soup.find('ul', class_="emoji-list")
        spans = ul.find_all('span', class_='emoji')
        symbols = [span.get_text() for span in spans]
    except:
        symbols = list()

    return symbols


def palette() -> dict:
    """Get dict of all categories and their corresponding emojis"""

    return dict([(c, category(c)) for c in categories])


def search(emoji: str) -> Emoji:
    """Get Emoji instance from given emoji string"""

    emoji_url = f"https://emojipedia.org/{urllib.parse.quote(emoji)}"

    page = requests.get(emoji_url)
    soup = BeautifulSoup(page.content, 'lxml')

    # Name
    symbol: str
    name: str
    try:
        heading = soup.find('article').find('h1').get_text()
        symbol = heading[0]
        name = heading[2:]
    except:
        symbol = ""
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
        aliases = [li.get_text().replace(f"{symbol} ", "")
                   for li in section_aliases.find('ul').find_all('li')]
    except:
        aliases = list()

    # Apple Name
    apple_name: str
    try:
        section_applenames = soup.find('section', class_="applenames")
        apple_name = section_applenames.find(
            'p').get_text().replace(f"{symbol} ", "")
    except:
        apple_name = ""

    # Unicode Name
    unicode_name: str
    try:
        section_unicodenames = soup.find('section', class_="unicodename")
        unicode_name = section_unicodenames.find(
            'p').get_text().replace(f"{symbol} ", "")
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
        'symbol': symbol,
        'description': description,
        'name': name,
        'aliases': aliases,
        'apple_name': apple_name,
        'unicode_name': unicode_name,
        'vendors': vendors
    }

    return Emoji(**emoji_info)
