include .env

export

# Deploy for cloud run using custom Dockerfile
deploy:
	gcloud run deploy $(SERVICE_NAME) \
		--port=8080 \
		--source="." \
		--region=$(GOOGLE_CLOUD_LOCATION) \
		--project=$(GOOGLE_CLOUD_PROJECT) \
		--allow-unauthenticated \
		--min-instances=1 \
		--cpu-boost \
		--execution-environment=gen2 \
		--set-env-vars=GOOGLE_ENTRYPOINT=$(GOOGLE_ENTRYPOINT),GOOGLE_GENAI_USE_VERTEXAI=$(GOOGLE_GENAI_USE_VERTEXAI),SERVICE_NAME=$(SERVICE_NAME),GOOGLE_API_KEY=$(GOOGLE_API_KEY),GOOGLE_CLOUD_PROJECT=$(GOOGLE_CLOUD_PROJECT),GOOGLE_CLOUD_LOCATION=$(GOOGLE_CLOUD_LOCATION),LOG_LEVEL=DEBUG

# Deploy for web ui version of the agent to Cloud Run on port 8000
# deploy:
# 	adk deploy cloud_run \
# 	--project=$$GOOGLE_CLOUD_PROJECT \
# 	--region=$$GOOGLE_CLOUD_LOCATION \
# 	--service_name=$$SERVICE_NAME \
# 	--app_name=$$APP_NAME \
# 	--with_ui \
# 	$$AGENT_PATH

