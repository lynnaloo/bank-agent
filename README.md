# Bank Card Services Agent

A multi-agent system built with Google's Agent Development Kit (ADK) for managing bank card services. This project demonstrates an agentic architecture where a root agent delegates card approval and cancellation tasks to specialized sub-agents.

## Overview

The Bank Card Services Agent is an intelligent system that processes credit card service requests by:
- Analyzing user inputs to determine the required action (approval or cancellation)
- Delegating to specialized sub-agents for specific tasks
- Updating customer records with the appropriate status
- Returning structured JSON responses with updated customer data

### Agent Architecture

**Root Agent (`card_services_agent`)**
- Main coordinator that welcomes users and understands their needs
- Determines whether a card should be approved or cancelled based on user inputs
- Delegates to the appropriate sub-agent
- Returns results in a clear, structured format

**Sub-Agents:**
- **Card Approver Agent** - Updates customer records to mark cards as approved
- **Card Canceller Agent** - Updates customer records to mark cards as cancelled

All agents use the `gemini-2.5-flash` model with optimized temperature and top_p settings for consistent, reliable responses.

## Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd bank-agent
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Copy the sample environment file and configure it:
```bash
cp sample.env .env
```

Edit `.env` with your credentials:
```bash
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_API_KEY=""  # Optional: for direct API access
```

## Configuration

### Google Cloud Setup

1. Enable the Vertex AI API in your Google Cloud project
2. Set up authentication:
   - For local development: `gcloud auth application-default login`
   - For production: Use service account credentials

3. Ensure your project has the necessary permissions for Vertex AI and Gemini models

### Customer Profiles

Sample customer profiles are located in `card_services_agent/profiles/`:
- `sample_customer.json` - Example customer with data
- `empty_customer.json` - Template for new customers

## Usage

### Running the Agent Locally

Start the ADK web interface:
```bash
adk web
```

This launches an interactive interface where you can:
- Test the agent with different customer requests
- View agent reasoning and sub-agent delegation
- See structured JSON responses

### Example Interactions

**Card Approval Request:**
```
"I'd like to approve the credit card for customer John Doe"
```

**Card Cancellation Request:**
```
"Please cancel the card for customer Jane Smith"
```

The root agent will:
1. Parse the request
2. Delegate to the appropriate sub-agent
3. Return the updated customer record with the status change

## Resources

* [ADK Agent ](https://google.github.io/adk-docs/get-started/python/)
* [Exposing an agent through A2A](https://google.github.io/adk-docs/a2a/quickstart-exposing/)