FROM python:3.13-slim

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY src/ src/

CMD ["poetry", "run", "openscience"]
