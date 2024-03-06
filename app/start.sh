#! /usr/bin/env sh
set -e

MODULE_NAME=${MODULE_NAME:-main}
VARIABLE_NAME=${VARIABLE_NAME:-app}
export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8000}
LOG_LEVEL=${LOG_LEVEL:-info}
LOGCONFIG=${LOGCONFIG:-"./logging.conf"}
WORKERS=${WORKERS:-1}

exec poetry run uvicorn \
  --host $HOST \
  --port $PORT \
  --log-level $LOG_LEVEL \
  --log-config $LOGCONFIG \
  --workers $WORKERS \
  --no-access-log \
  --reload \
  "$APP_MODULE"
