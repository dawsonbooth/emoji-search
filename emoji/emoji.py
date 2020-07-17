from typing import List


class Emoji:
    """Class containing miscellaneous information to do with given emoji"""

    __slots__ = 'symbol', 'description', 'name', 'aliases', 'apple_name', 'unicode_name', 'vendors'

    def __init__(self, **kwargs):
        for (key, value) in kwargs.items():
            self.__setattr__(key, value)

    def __iter__(self):
        for key in self.__slots__:
            value = getattr(self, key, None)
            yield key, value


categories: List[str] = ['people', 'nature', 'food-drink',
                         'activity', 'travel-places', 'objects', 'symbols', 'flags']
