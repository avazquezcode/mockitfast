setup:
	cp .env.dist .env

build:
	docker-compose build

run:
	docker-compose up -d
