# ./Dockerfile.prod
FROM python:3.9-slim as builder

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.9-slim
WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/app

RUN python manage.py collectstatic --noinput

CMD ["sh", "entrypoint.sh"]