.PHONY: clean test build dist environment install uninstall reinstall

clean:
	rm -rf *.o *.out *.log
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +

test:
	pytest

build:
	python -m build

dist:
	make build
	twine upload dist/*

environment:
	mamba create -y -n VIIRS-Swath-Granules python=3.11 jupyter pykdtree

install:
	pip install -e .[dev]

uninstall:
	pip uninstall -y VIIRS-Swath-Granules

reinstall: uninstall install