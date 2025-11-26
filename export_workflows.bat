@echo off
echo -----------------------------------------
echo Exporting all n8n workflows to /workflows
echo -----------------------------------------

docker exec -u node -it n8n n8n export:workflow --all --separate --output=/home/node/workflows

echo.
echo Done! Workflows saved in the local "workflows" folder.
pause
