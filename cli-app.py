import matlab.engine
eng = matlab.engine.start_matlab()

from models import llm
from tools import tools
from prompts import prompt

from langchain.agents import AgentExecutor, create_react_agent

agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
                                agent = agent,
                                tools = tools,
                                verbose = True,
                                handle_parsing_errors = True,
                                max_execution_time = 300,
                                max_iterations = 20,
                            )

chat_messages = []
user_messge = input("\nUser: ")

while user_messge != "bye":

    response = agent_executor.invoke({"input": user_messge, "chat_history": chat_messages})

    chat_messages.append(("user",      response["input"]))
    chat_messages.append(("assistant", response["output"]))

    user_messge = input("\nUser: ")

eng.quit()