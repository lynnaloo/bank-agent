# Start with a standard Python base image
FROM python:3.11-slim
# Set working directory inside the container
WORKDIR /app

# Create a non-root user
RUN adduser --disabled-password --gecos "" myuser

# Install dependencies as root to avoid permission issues
RUN pip install --no-cache-dir \
    "google-adk[a2a]>=0.18.0" \
    "google-generativeai>=0.8.0" \
    "google-cloud-aiplatform>=1.38.0"

# Copy application code with proper ownership
COPY --chown=myuser:myuser . /app/card_services_agent/

# Switch to the non-root user
USER myuser

# Set up environment variables - Start
ENV PATH="/home/myuser/.local/bin:$PATH"

ENV GOOGLE_GENAI_USE_VERTEXAI=1
ENV GOOGLE_CLOUD_PROJECT=salesforce-demo-linda
ENV GOOGLE_CLOUD_LOCATION=us-central1

# Set up environment variables - End

EXPOSE 8001

# Use Uvicorn to serve the application
# main:a2a_app references your main.py file and the 'a2a_app' variable defined within it
CMD exec uvicorn main:a2a_app --host 0.0.0.0 --port 8001