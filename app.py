import matlab.engine
eng = matlab.engine.start_matlab()

from agent import agent_executor

chat_messages = []
user_messge = input("\nUser: ")

while user_messge != "bye":
    response = agent_executor.invoke({"input": user_messge, "chat_history": chat_messages})
    chat_messages.append(("user",      response["input"]))
    chat_messages.append(("assistant", response["output"]))
    user_messge = input("\nUser: ")

eng.quit()