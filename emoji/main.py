import argparse
import json

from . import Emoji, categories, category, palette, search


def main():
    parser = argparse.ArgumentParser(
        description='Search for emoji information')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--search', type=str, required=False, default="",
                       help='Emoji to search for')
    group.add_argument('--category', type=str, required=False, default="",
                       help='Category to get list of emojis')
    group.add_argument('--categories', required=False, action='store_true', default=False,
                       help='Get list of emoji categories')
    group.add_argument('--palette', required=False, action='store_true', default=False,
                       help='Get JSON object of all categories and their emojis')

    args = parser.parse_args()

    if args.search:
        print(json.dumps(dict(search(args.search)), ensure_ascii=False))
    elif args.category:
        print(category(args.category))
    elif args.palette:
        print(json.dumps(dict(palette()), ensure_ascii=False))
    elif args.categories:
        print(categories)
    else:
        parser.error("Invalid command")


if __name__ == "__main__":
    main()
