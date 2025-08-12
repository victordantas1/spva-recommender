#!/bin/bash

set -e

if [[ -z "$1" ]]; then
  echo "ERRO: É necessário especificar o ambiente."
  echo "Uso: ./run.sh [dev|prod]"
  exit 1
fi

ENVIRONMENT=$(echo "$1" | tr '[:upper:]' '[:lower:]')

if [[ "$ENVIRONMENT" == "dev" ]]; then
  echo "--- INICIANDO EM MODO DE DESENVOLVIMENTO ---"

  if [[ ! -f .env ]]; then
    echo "AVISO: Arquivo .env não encontrado. As variáveis de ambiente podem não estar setadas."
  else
    echo "-> Carregando variáveis de ambiente do arquivo .env..."
    export $(grep -v '^#' .env | xargs)
    echo "-> Variáveis carregadas."
  fi

  echo "-> Rodando Uvicorn com hot-reload na porta ${PORT}..."
  uvicorn src.main:app --host 0.0.0.0 --port ${PORT} --reload

elif [[ "$ENVIRONMENT" == "prod" ]]; then
  echo "--- INICIANDO EM MODO DE PRODUÇÃO ---"
  echo "AVISO: Certifique-se que as variáveis de ambiente (DATABASE_URL, etc.) foram setadas externamente."

  WORKERS=${WORKERS:-4}
  PORT=${PORT:-8001}

  echo "-> Rodando Gunicorn com $WORKERS workers Uvicorn na porta $PORT..."
  gunicorn -w $WORKERS -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT src.main:app

else
  echo "ERRO: Ambiente '$1' não reconhecido. Use 'dev' ou 'prod'."
  exit 1
fi