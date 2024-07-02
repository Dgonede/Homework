FROM python:3.12.3-bookworm

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install "poetry==1.8.3" setuptools wheel

RUN poetry config virtualenvs.create false

RUN pip install fastapi uvicorn

COPY pyproject.toml .

COPY poetry.lock .

COPY homework_03 ./

CMD ["uvicorn", "main:app", "--host",  "0.0.0.0", "--port", "5000"]

EXPOSE 5000