setup:
	cp .env.dist .env

build:
	docker-compose build

run:
	docker-compose up -d

logs:
	docker logs -f mockitfast_app