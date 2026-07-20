FROM python:3.13-alpine

WORKDIR /app
COPY server.py .

RUN addgroup -S app && adduser -S app -G app
USER app

EXPOSE 8000
HEALTHCHECK --interval=10s --timeout=3s --retries=3   CMD wget -q -O - http://localhost:8000/health || exit 1

CMD ["python", "server.py"]
