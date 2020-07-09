import argparse
from emoji import Emoji, search, palette, category
import json


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Search for emoji information')
    parser.add_argument('--search', type=str, required=False, default="",
                        help='Emoji to search for')
    parser.add_argument('--category', type=str, required=False, default="",
                        help='Category of emojis')
    parser.add_argument('--palette', required=False, action='store_true', default=False,
                        help='Palette of emojis')

    args = parser.parse_args()

    try:
        if args.search:
            print(json.dumps(dict(search(args.keyword)), ensure_ascii=False))
        elif args.category:
            print(category(args.keyword))
        elif args.palette:
            print(json.dumps(dict(palette()), ensure_ascii=False))
        else:
            raise Exception()
    except:
        parser.error("Invalid command")
