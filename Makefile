activate:
	. .venv/bin/activate;

setup:
	cp .env.dist .env

build: activate
	pip install -r requirements.txt

run: activate
	python src/main.py
