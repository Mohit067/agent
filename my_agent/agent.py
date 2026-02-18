import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent


from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams, StreamableHTTPConnectionParams
from google.adk.agents import LlmAgent
from mcp import StdioServerParameters

PATH_OF_MCP_SERVER_SCRIPT = r"C:\Users\MM0956\Documents\Expense-tracker-MCP\main.py"
load_dotenv()

# DATABASE_AGENT_URL = "http://190.1.3.74:8001/"
DATABASE_AGENT_URL = "http://localhost:8001/"

remote_agent = RemoteA2aAgent(
    name="DB_Sales_Chart_Agent",
    description="Root agent to orchestrate Database Agent, Sales and Chart Agent.",
    agent_card=f"{DATABASE_AGENT_URL}{AGENT_CARD_WELL_KNOWN_PATH}",
)

add_two_numbers = LlmAgent(
    model=LiteLlm(model="groq/openai/gpt-oss-20b"),
    name='add_agent',
    instruction="Use the 'add_two_numbers'  tool to add the number given by the user.",
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command='uv',
                    args=['run', PATH_OF_MCP_SERVER_SCRIPT],
                )
            )
        )
    ],
)

# add_two_numbers = LlmAgent(
#     model=LiteLlm(model="groq/openai/gpt-oss-20b"),
#     name='add_agent',
#     instruction="Use the 'add_two_numbers'  tool to add the number given by the user.",
#     tools=[
#         McpToolset(
#             connection_params=StdioConnectionParams(
#                 server_params=StdioServerParameters(
#                     command='uv',
#                     args=['run', PATH_OF_MCP_SERVER_SCRIPT],
#                 )
#             )
#         )
#     ],
# )

root_agent = Agent(
    model=LiteLlm(model="groq/openai/gpt-oss-20b"),
    name='Orchestrator_Agent',
    description="""You are "Maventic" the Orchestrator agent.""",
    instruction='Answer user questions to the best of your knowledge, use the tools and sub agents to perform tasks based on the user requirements. whenever the sum of two number is required use "add_agent" agent',
    sub_agents=[remote_agent,add_two_numbers],
)
