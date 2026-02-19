FROM python:3.14-slim
LABEL org.opencontainers.image.source="https://github.com/deydoux/addy.io2hme"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app app

CMD ["fastapi", "run", "app"]
