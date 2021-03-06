FROM python:3.7

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv \
 && pipenv install --system

COPY . ./

CMD cd app && python app.py
