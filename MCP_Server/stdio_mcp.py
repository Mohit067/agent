import random
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("MyAssistantServer")


@mcp.tool()
def add_two_numbers(a: float, b: float) -> str:
    """Add two numbers together and return the result."""
    result = a + b
    return f"{a} + {b} = {result}"


if __name__ == "__main__":
    mcp.run()
