setup:
	cp .env.dist .env

build:
	docker-compose build

run:
	docker-compose up -d

build_run:
	docker-compose up -d --build

logs:
	docker logs -f mockitfast_app

test:
	python3 -m unittest discover -s src -p 'test_*.py'

