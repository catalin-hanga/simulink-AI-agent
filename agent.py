from models import llm
from tools import tools
from prompts import prompt

from langchain.agents import create_react_agent, AgentExecutor 

agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
                                agent = agent,
                                tools = tools,
                                verbose = True,
                                handle_parsing_errors = True,
                                max_execution_time = 300,
                                max_iterations = 20,
                            )