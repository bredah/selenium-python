FROM python:3.11-slim-bullseye

RUN apt update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /automation

COPY . .

RUN poetry config virtualenvs.create false && \
    poetry install --no-root

ENTRYPOINT ["poetry", "run"]
