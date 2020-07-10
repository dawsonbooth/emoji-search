# `emoji-search`


[![](https://img.shields.io/pypi/v/emoji-search.svg?style=flat)](https://pypi.org/pypi/emoji-search/)
[![](https://img.shields.io/pypi/dw/emoji-search.svg?style=flat)](https://pypi.org/pypi/emoji-search/)
[![](https://img.shields.io/pypi/pyversions/emoji-search.svg?style=flat)](https://pypi.org/pypi/emoji-search/)
[![](https://img.shields.io/pypi/format/emoji-search.svg?style=flat)](https://pypi.org/pypi/emoji-search/)
[![](https://img.shields.io/pypi/l/emoji-search.svg?style=flat)](https://github.com/dawsonbooth/emoji-search/blob/master/LICENSE)


*The #1 Python tool for miscellaneous emoji info*


# Installation

With [Python](https://www.python.org/downloads/) installed, simply run the following command to add the package to your project.

```bash
pip install emoji-search
```

# Usage

The following is an example usage of the package:

```python
from random import choice
from emoji import Emoji, categories, search, category

def random_emoji() -> Emoji:
    return search(choice(category(choice(categories))))

print(random_emoji())
```

You can also run the tool from the command-line:

```txt
usage: console.py [-h] [--search SEARCH | --category CATEGORY | --categories | --palette]

Search for emoji information

optional arguments:
  -h, --help           show this help message and exit
  --search SEARCH      Emoji to search for
  --category CATEGORY  Category to get list of emojis
  --categories         Get list of emoji categories
  --palette            Get JSON object of all categories and their emojis
```

```bash
emoji-search --search '🎈' > balloon.json
```
Then check out all the information!

```json
{
  "symbol": "🎈",
  "description": "A balloon on a string, as decorates a birthday party. Generally depicted in red, though WhatsApp’s is pink and Google’s orangish-red.\nCommonly used to convey congratulations and celebration, especially when wishing someone a happy birthday.\nMicrosoft and Samsung's balloons were previously blue; SoftBank's was shown floating in the sky.\n\nBalloon was approved as part of Unicode 6.0 in 2010\nand added to Emoji 1.0 in 2015.\n",
  "name": "Balloon",
  "aliases": ["Party", "Red Balloon"],
  "apple_name": "Balloon",
  "unicode_name": "",
  "vendors": {
    "Apple": [
      "iOS 13.3",
      "iOS 10.2",
      "iOS 8.3",
      "iOS 6.0",
      "iOS 5.1",
      "iOS 4.0",
      "iPhone OS 2.2"
    ],
    "Google": [
      "Android 10.0 March 2020 Feature Drop",
      "Android 8.0",
      "Android 7.0",
      "Android 5.0",
      "Android 4.4",
      "Android 4.3"
    ],
    "Microsoft": [
      "Windows 10 May 2019 Update",
      "Windows 10 Anniversary Update",
      "Windows 10",
      "Windows 8.1",
      "Windows 8.0"
    ],
    "Samsung": [
      "One UI 1.5",
      "One UI 1.0",
      "Experience 9.0",
      "Experience 8.0",
      "TouchWiz 7.1",
      "TouchWiz 7.0",
      "TouchWiz Nature UX 2"
    ],
    "WhatsApp": ["2.19.352", "2.17"],
    "Twitter": ["Twemoji 13.0", "Twemoji 1.0"],
    "Facebook": ["4.0", "3.0", "2.0", "1.0"],
    "JoyPixels": [
      "6.0",
      "5.5",
      "5.0",
      "4.5",
      "4.0",
      "3.1",
      "3.0",
      "2.2",
      "2.0",
      "1.0"
    ],
    "OpenMoji": ["12.3", "1.0"],
    "emojidex": ["1.0.34", "1.0.33", "1.0.19", "1.0.14"],
    "Messenger": ["1.0"],
    "LG": ["G5", "G3"],
    "HTC": ["Sense 7"],
    "Mozilla": ["Firefox OS 2.5"],
    "SoftBank": ["2014", "2008", "2006", "2004", "2001", "2000"],
    "Docomo": ["2013"],
    "au by KDDI": ["Type F", "Type D-3", "Type D-2", "Type D-1"]
  }
}
```

# License

This software is released under the terms of [MIT license](LICENSE).
