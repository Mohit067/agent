from dotenv import load_dotenv
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from .tools.database import db_tools
from .tools.chart import generate_chart

load_dotenv()

# Database agent who will perform database operations like CRUD based on the user query.
database_agent = Agent(
    name='Database_Agent',
    model=LiteLlm(model="groq/openai/gpt-oss-20b"),
    description='Database agent is an AI agent capable of db operations on the server. It can perform insertions, deletions, updations and retrival from that database.',
    instruction='Answer user questions to the best of your knowledge, use relavant tools that perform SQL queries in the database. You are a Database agent capable of db operations on the server. It can perform insertions, deletions, updations and retrival from that database.',
    tools=db_tools,
)

# chart agent who will generate chart based on the data provided by the user
chart_agent = Agent(
    name="Sales_Chart_Agent",
    model=LiteLlm(model="groq/openai/gpt-oss-20b"),
    description="Sales Chart Agent is an AI agent capable of generating "
        "monthly revenue charts using provided sales data.",
    instruction="You are a Sales Chart Agent. "
        "If the user provides monthly sales data, "
        "extract the month and revenue values correctly "
        "and use the generate_chart tool to create the chart. "
        "Ensure the data format is a list of tuples like "
        "[('Jan', 1000), ('Feb', 1500)].",
    tools=[generate_chart],
)

# Root agent that orchestrates both subagents
root_agent = Agent(
    name="Root_Agent",
    description="Root agent to orchestrate Database Agent, Sales Chart Agent and Summary Agent.",
    instruction="You are the Root Agent. Route tasks to Database Agent, chart agent based on the user's query.",
    sub_agents=[database_agent, chart_agent],
)

# Establishing A2A communication for the root agent on port 8001
a2a_app = to_a2a(root_agent, port=8001)