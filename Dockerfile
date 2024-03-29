FROM python:3.8.12-buster

ARG POETRY_VERSION=1.1.12

COPY poetry.lock .
COPY pyproject.toml .
COPY app app/
COPY .streamlit/ ~/.streamlit/

RUN pip install poetry==$POETRY_VERSION
RUN poetry config virtualenvs.create false && poetry install

CMD ["streamlit", "run", "app/app.py"]
