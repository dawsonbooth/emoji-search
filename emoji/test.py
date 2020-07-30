from .emoji import Emoji, categories
from .search import category, palette, search


def test_categories():
	assert len(categories) > 0

def test_category():
	assert len(category(categories[0])) > 0

def test_palette():
	assert len(palette()) > 0

def test_search():
	assert isinstance(search('🤯'), Emoji)
