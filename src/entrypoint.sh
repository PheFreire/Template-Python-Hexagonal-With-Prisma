#!/bin/bash

curl -sSL https://install.python-poetry.org | python3 -
export PATH="/root/.local/bin:$PATH"
poetry env use python3
poetry install
echo "Executando comando poetry ...."
make run
