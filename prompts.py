from langchain.prompts import PromptTemplate

template = """
Answer the following questions as best you can. You have access to the following tools:

{tools}

You also have access to the following conversation history with the user:

{chat_history}

Please use the following format:
    
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (if necessary, this Thought/Action/Action Input/Observation cycle can be repeated several times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question
    
Begin!
    
Question: {input}
Thought: {agent_scratchpad}
"""

prompt = PromptTemplate(
                        template = template,
                        input_variables = ["input", "tools", "tool_names", "chat_history", "agent_scratchpad"],
                        )