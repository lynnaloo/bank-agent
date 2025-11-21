import os
from google.adk.agents import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from a2a.types import AgentCard
from google.genai.types import GenerateContentConfig

from card_services_agent import prompt
from card_services_agent.tools.card_ops import approve_card, cancel_card

# Get port and host from environment variables, with defaults
port = int(os.getenv('PORT', '8001'))
host = os.getenv('HOST_OVERRIDE', 'localhost')

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='An agent that performs card service actions like approving or cancelling credit cards based on user input.',
    instruction=prompt.ROOT_AGENT_INSTR,
    tools=[approve_card, cancel_card],
    output_key='result',
    generate_content_config=GenerateContentConfig(
        temperature=0.0
    )
)

# Make your agent A2A-compatible
a2a_app = to_a2a(root_agent, port=port, host=host)