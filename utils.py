from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
                    model = "gpt-4o-mini",
                    temperature = 0,
                    streaming = True,           
                )