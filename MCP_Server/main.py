import random
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("MyAssistantServer")


@mcp.tool()
def roll_dice(sides: int = 6) -> str:
    """Roll a dice with the given number of sides (default is 6)."""
    result = random.randint(1, sides)
    return f"🎲 You rolled a {result} (out of {sides} sides)!"


@mcp.tool()
def add_two_numbers(a: float, b: float) -> str:
    """Add two numbers together and return the result."""
    result = a + b
    return f"➕ {a} + {b} = {result}"


if __name__ == "__main__":
    mcp.run()
