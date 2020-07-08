import argparse
from emoji import search
import json


def main(emoji):
    try:
        return search(emoji)
    except KeyboardInterrupt:
        print("Terminated.")
        exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Search for emoji information')
    parser.add_argument('emoji', type=str,
                        help='The emoji to search for')

    args = parser.parse_args()

    print(json.dumps(main(args.emoji), ensure_ascii=False))
