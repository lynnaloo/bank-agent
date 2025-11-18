FROM python:3.11-slim
WORKDIR /app

# Create a non-root user
RUN adduser --disabled-password --gecos "" myuser

# Switch to the non-root user
USER myuser

# Set up environment variables 
ENV PATH="/home/myuser/.local/bin:$PATH"

# ENV GOOGLE_GENAI_USE_VERTEXAI=1
# ENV GOOGLE_CLOUD_PROJECT=salesforce-demo-linda
# ENV GOOGLE_CLOUD_LOCATION=us-central1

# Install dependencies as root to avoid permission issues
RUN pip install --no-cache-dir \
    "google-adk[a2a]>=0.18.0" \
    "google-generativeai>=0.8.0" \
    "google-cloud-aiplatform>=1.38.0"

# Copy agent
# Set permission
COPY --chown=myuser:myuser "agents/card_services_agent" "/app/card_services_agent"

EXPOSE 8080
CMD exec uvicorn card_services_agent.agent:a2a_app --host 0.0.0.0 --port $PORT