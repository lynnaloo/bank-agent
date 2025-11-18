include .env

export

deploy:
	adk deploy cloud_run \
	--a2a \
	--project=$$GOOGLE_CLOUD_PROJECT \
	--region=$$GOOGLE_CLOUD_LOCATION \
	--service_name=$$SERVICE_NAME \
	--app_name=$$APP_NAME \
	--port=8080 \
	--with_ui \
	$$AGENT_PATH
