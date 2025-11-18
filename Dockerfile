
FROM python:3.11-slim
WORKDIR /app

# Create a non-root user
RUN adduser --disabled-password --gecos "" myuser

# Switch to the non-root user
USER myuser

# Set up environment variables - Start
ENV PATH="/home/myuser/.local/bin:$PATH"

# Install ADK - Start
RUN pip install --no-cache-dir \
    "google-adk[a2a]>=0.18.0" \
    "google-generativeai>=0.8.0" \
    "google-cloud-aiplatform>=1.38.0"

# Set permission
COPY --chown=myuser:myuser "agents/card_services_agent" "/app/card_services_agent"

EXPOSE 8080

#CMD adk web --port=8080 --host=0.0.0.0      --a2a "/app/agents"
CMD exec uvicorn card_services_agent.agent:a2a_app --host 0.0.0.0 --port $PORT