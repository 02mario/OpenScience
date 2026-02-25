FROM python:3.13-slim

ENV POETRY_HOME="/etc/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY src/ src/

CMD ["poetry", "run", "python", "-m", "src.main", "--grobid_url", "http://grobid:8070"]
