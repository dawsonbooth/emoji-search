
Python 2.7 will no longer be supported in the next feature release of Poetry (1.2).
You should consider updating your Python version to a supported one.

Note that you will still be able to manage Python 2.7 projects by using the env command.
See https://python-poetry.org/docs/managing-environments/ for more information.

<a name="emoji"></a>
# emoji

<a name="emoji.emoji"></a>
# emoji.emoji

<a name="emoji.emoji.Emoji"></a>
## Emoji Objects

```python
class Emoji()
```

Class containing miscellaneous information to do with given emoji

<a name="emoji.test"></a>
# emoji.test

<a name="emoji.search"></a>
# emoji.search

<a name="emoji.search.category"></a>
#### category

```python
category(category: str) -> List[str]
```

Get list of emojis in the given category

<a name="emoji.search.palette"></a>
#### palette

```python
palette() -> dict
```

Get dict of all categories and their corresponding emojis

<a name="emoji.search.search"></a>
#### search

```python
search(emoji: str) -> Emoji
```

Get Emoji instance from given emoji string

<a name="emoji.main"></a>
# emoji.main

