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
	python setup.py sdist

dist:
	make build
	twine upload dist/*

install:
	pip install -e .

uninstall:
	pip uninstall -y VIIRS-Swath-Granules
