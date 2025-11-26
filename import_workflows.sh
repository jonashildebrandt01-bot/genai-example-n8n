#!/bin/bash

echo "-----------------------------------------"
echo "Importing workflows from /workflows"
echo "-----------------------------------------"

docker exec -u node -it n8n \
  n8n import:workflow --separate --input=/home/node/workflows

echo ""
echo "Done! Workflows imported into n8n."
