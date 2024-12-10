# Contributing

This file contains a guideline about how to build the app in the local machine, and execute it.

## Build

> **_NOTE:_**  Later on I will also configure docker to build & run the project easily

**For now:**

1) **Pre-requisite**: Make sure to have **python** installed
2) Run `python -m venv .venv` to create a .venv, and then: `source .venv/bin/activate` (**Every time you install a new package you should activate the environment.**)
3) Run `echo "*" > .venv/.gitignore` to setup gitignore in venv
4) Run `make setup` & edit the variables in `.env` file
5) Run `make build`


## Start

Run `make run`

## Router config

> **_NOTE:_**  Later on I will create a documentation specifying exactly the capabilities / supported options.

You can configure your mocked API in the [router.json](./router.json) file.
You can modify it on the run, while the service is running and the changes will be impacted on runtime. This is achieved using a really simple [file watcher](./src/watcher.py)

## Swagger

> **_NOTE:_**  The following URL might change depending on what is configured in your .env file.

After running the project you can access the swagger of your mocked API going to: [localhost:3000/docs](localhost:3000/docs)