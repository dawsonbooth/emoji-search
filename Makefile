VERSION := $(shell poetry version | grep -oE '[^ ]+$$')

.PHONY: all list clean lint test docs build publish version

all: list

list:
	@sh -c "$(MAKE) -p no_targets__ | \
		awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {\
			split(\$$1,A,/ /);for(i in A)print A[i]\
		}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"

clean:
	rm -rf build/ dist/
	rm -f *.spec
	@poetry run pyclean .

lint:
	@poetry run pylint emoji

test:
	@poetry run pytest emoji/test.py

docs:
	@poetry run pydoc-markdown -p emoji > docs/documentation.md
	@cp README.md docs/README.md
	@poetry run mkdocs build --clean

build:
	@poetry build

publish:
	@poetry run mkdocs gh-deploy
	@poetry publish

version:
	@echo $(VERSION)
	