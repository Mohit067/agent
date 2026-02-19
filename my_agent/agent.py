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

load_dotenv()

PATH_OF_MCP_SERVER_SCRIPT = os.getenv('PATH_OF_MCP_SERVER_SCRIPT')
MCP_SERVER_URL=os.getenv('MCP_SERVER_URL')
DATABASE_AGENT_URL = os.getenv('DATABASE_AGENT_URL')
# DATABASE_AGENT_URL = "http://localhost:8001/"

remote_agent = RemoteA2aAgent(
    name="DB_Sales_Chart_Text_Agent",
    description="Remote agent to perform database operations and generate charts. and summarize the text.",
    agent_card=f"{DATABASE_AGENT_URL}{AGENT_CARD_WELL_KNOWN_PATH}",
)

# add_tow_numeber Agent that communicates to the HTTP MCP server
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

# Summarizer Agent that communicates to the HTTP MCP server
summarize_agent = LlmAgent(
    model=LiteLlm(model="groq/openai/gpt-oss-20b"),
    name='summarize_agent',
    instruction="You are a summarizer agent who take user message or text and summarize that text",
    tools=[
        McpToolset(
            connection_params=StreamableHTTPConnectionParams(
                url=MCP_SERVER_URL
            )
        )
    ],
)

root_agent = Agent(
    model=LiteLlm(model="groq/openai/gpt-oss-20b"),
    name='Orchestrator_Agent',
    description="""You are "Maventic" the Orchestrator agent.""",
    instruction='Answer user questions to the best of your knowledge, use the tools and sub agents to perform tasks based on the user requirements. whenever the sum of two number is required use "add_agent" agent',
    sub_agents=[remote_agent,add_two_numbers,summarize_agent],
)
