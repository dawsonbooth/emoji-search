import argparse
import json

from emoji import Emoji, all, category, search


def main():
    parser = argparse.ArgumentParser(
        description='Search for emoji information')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--search', type=str, required=False, default="",
                       help='Emoji to search for')
    group.add_argument('--category', type=str, required=False, default="",
                       help='Category to get list of emojis')
    group.add_argument('--all', required=False, action='store_true', default=False,
                       help='Get palette of all categories and their emojis')

    args = parser.parse_args()

    if args.search:
        print(json.dumps(dict(search(args.search)), ensure_ascii=False))
    elif args.category:
        print(category(args.category))
    elif args.all:
        print(json.dumps(dict(all()), ensure_ascii=False))
    else:
        parser.error("Invalid command")


if __name__ == "__main__":
    main()
