FROM python:3.11

USER root

WORKDIR /app

ADD . .

ENTRYPOINT ["/bin/bash", "src/entrypoint.sh"]

EXPOSE 8000

