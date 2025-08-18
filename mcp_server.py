from functions import functions
from mcp.server.fastmcp import FastMCP

import matlab.engine
eng = matlab.engine.start_matlab()

# Initialize FastMCP server
mcp = FastMCP(name = "simulang")

# Add tools to the server
for func in functions:
    mcp.add_tool(func)

if __name__ == "__main__":
    # Initialize and run the server locally
    mcp.run(transport='stdio')