from models import llm
from prompts import prompt
from functions import functions
from langchain_core.tools import StructuredTool
from langchain.agents import create_react_agent, AgentExecutor 

tools = []

for func in functions:
   tool = StructuredTool.from_function(func = func)
   tools.append(tool)

agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
                                agent = agent,
                                tools = tools,
                                verbose = True,
                                handle_parsing_errors = True,
                                max_execution_time = 300,
                                max_iterations = 20,
                            )