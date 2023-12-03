FROM python:3.10

WORKDIR /code

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./assistant /code/assistant

EXPOSE 8080