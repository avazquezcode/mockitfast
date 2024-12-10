venv: venv/touchfile

activate:
	. .venv/bin/activate;

build: activate
	pip install -r requirements.txt

run: activate
	python src/main.py
