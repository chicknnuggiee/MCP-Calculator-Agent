from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Calculator Agent")


@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


@mcp.tool()
def subtract_numbers(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


@mcp.tool()
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b


@mcp.tool()
def divide_numbers(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    mcp.run()