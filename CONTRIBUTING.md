# Contributing

This file contains a guideline about how to build the app in the local machine, and execute it.

## Build

> **_NOTE:_**  Later on I will also configure docker to build & run the project easily

**For now:**

1) **Pre-requisite**: Make sure to have **python3** installed
3) Run `make setup` & edit the variables in `.env` file
2) Run `make build`

## Run
Run `make run`

## Router config

> **_NOTE:_**  Later on I will create a documentation specifying exactly the capabilities / supported options.

You can configure your mocked API in the [router.json](./router.json) file.

## Swagger

> **_NOTE:_**  The following URL might change depending on what you configure in your .env file.

After running the project you can access the swagger of your mocked API going to: [localhost:3000/docs](localhost:3000/docs)