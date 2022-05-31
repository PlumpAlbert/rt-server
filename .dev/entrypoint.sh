#!/bin/sh
source /app/.venv/bin/activate
cd /app
source /app/.env
gunicorn -c "${GUNICORN_CONFIG}"
