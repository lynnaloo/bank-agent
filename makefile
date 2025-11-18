include .env

export

# Deploy for web ui version of the agent to Cloud Run on port 8000
# deploy:
# 	adk deploy cloud_run \
# 	--project=$$GOOGLE_CLOUD_PROJECT \
# 	--region=$$GOOGLE_CLOUD_LOCATION \
# 	--service_name=$$SERVICE_NAME \
# 	--app_name=$$APP_NAME \
# 	--with_ui \
# 	$$AGENT_PATH

# Deploy for a2a API server version of the agent to Cloud Run on port 8080
deploy:
	adk deploy cloud_run \
	--a2a \
	--port=8080 \
	--project=$$GOOGLE_CLOUD_PROJECT \
	--region=$$GOOGLE_CLOUD_LOCATION \
	--service_name=$$SERVICE_NAME \
	--app_name=$$APP_NAME \
	$$AGENT_PATH

# Deploy for a2a version of the agent to Cloud Run on port 8080
# deploy:
# 	docker build --tag $(SERVICE_NAME)-image .

# 	gcloud auth configure-docker $(GOOGLE_CLOUD_LOCATION)-docker.pkg.dev
# 	docker tag $(SERVICE_NAME)-image $(GOOGLE_CLOUD_LOCATION)-docker.pkg.dev/$(GOOGLE_CLOUD_PROJECT)/$(REPO_NAME)/$(IMAGE_NAME):latest
# 	docker push $(GOOGLE_CLOUD_LOCATION)-docker.pkg.dev/$(GOOGLE_CLOUD_PROJECT)/$(REPO_NAME)/$(IMAGE_NAME):latest

# 	gcloud run deploy $(SERVICE_NAME) \
# 		--image=$(GOOGLE_CLOUD_LOCATION)-docker.pkg.dev/$(GOOGLE_CLOUD_PROJECT)/$(REPO_NAME)/$(IMAGE_NAME):latest \
# 		--region=$(GOOGLE_CLOUD_LOCATION) \
# 		--platform=managed \
# 		--set-env-vars="HOST_OVERRIDE=$(HOST_OVERRIDE),GOOGLE_GENAI_USE_VERTEXAI=$(GOOGLE_GENAI_USE_VERTEXAI),GOOGLE_CLOUD_PROJECT=$(GOOGLE_CLOUD_PROJECT),GOOGLE_CLOUD_LOCATION=$(GOOGLE_CLOUD_LOCATION)" \
# 		--port=8080 \
# 		--project=$(GOOGLE_CLOUD_PROJECT)

# gcloud run deploy $(SERVICE_NAME) \
#     --port=8080 \
#     --source="." \
#     --region=REGION \
#     --project=PROJECT_ID \
#     --memory=1Gi \
#     --service-account=$$SERVICE_NAME \
#     --set-env-vars=GOOGLE_GENAI_USE_VERTEXAI=true,\
#       GOOGLE_CLOUD_PROJECT=$(GOOGLE_CLOUD_PROJECT),\
#       GOOGLE_CLOUD_LOCATION=$(GOOGLE_CLOUD_LOCATION),\
#       APP_URL="https://$(SERVICE_NAME)-$(GOOGLE_CLOUD_PROJECT).$(GOOGLE_CLOUD_LOCATION).run.app"

