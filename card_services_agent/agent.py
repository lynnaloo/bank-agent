from google.adk.agents import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from a2a.types import AgentCard

from card_services_agent import prompt
from card_services_agent.sub_agents.card_canceller.agent import card_canceller_agent
from card_services_agent.sub_agents.card_approver.agent import card_approver_agent
from card_services_agent.tools.memory import _load_customer

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='An agent that determines the appropriate card service actions',
    instruction=prompt.ROOT_AGENT_INSTR,
    sub_agents=[
        card_canceller_agent,
        card_approver_agent
    ]
    #before_agent_callback=_load_customer
)

# Define A2A agent card
# my_agent_card = AgentCard(
#     "name": "card_services_agent",
#     "url": "http://example.com",
#     "description": "Test agent from file",
#     "version": "1.0.0",
#     "capabilities": {},
#     "skills": [],
#     "defaultInputModes": ["text/plain"],
#     "defaultOutputModes": ["text/plain"],
#     "supportsAuthenticatedExtendedCard": False,
# )

# Make your agent A2A-compatible
a2a_app = to_a2a(root_agent, port=8001)