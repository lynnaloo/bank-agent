from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.genai.types import GenerateContentConfig

from card_services_agent.sub_agents.card_canceller import prompt

card_canceller_agent = Agent(
    model="gemini-2.5-flash",
    name="card_canceller_agent",
    description="""
    This agent updates a field in a record to indicate that the card is cancelled and returns a result in a structured JSON format.
    """,
    instruction=prompt.CARD_CANCELLER_AGENT_INSTR,
    tools=[],
    generate_content_config=GenerateContentConfig(
        temperature=0.1, top_p=0.5
    )
)