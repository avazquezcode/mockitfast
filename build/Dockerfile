FROM python:3.13.1

WORKDIR /code

ENV PYTHONPATH=/code/src/.

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

CMD ["python", "src/main.py"]