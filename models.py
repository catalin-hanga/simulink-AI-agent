from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
                    model = "gpt-4o-mini",
                    temperature = 0,
                )

# from langchain_openai import AzureChatOpenAI
# llm = AzureChatOpenAI(
#     azure_deployment = ...,  # your deployment
#     api_version = ... ,      # your api version
#     temperature = 0,
# )

# from langchain_anthropic import ChatAnthropic
# llm = ChatAnthropic(
#     model="claude-3-5-sonnet-20240620",
#     temperature=0,
# )

# from langchain_mistralai import ChatMistralAI
# llm = ChatMistralAI(
#     model="mistral-large-latest",
#     temperature=0,
# )

# from langchain_cohere import ChatCohere
# llm = ChatCohere()

# from langchain_aws import ChatBedrockConverse
# llm = ChatBedrockConverse(
#     model_id="meta.llama3-2-90b-instruct-v1:0",
#     temperature=0,
# )

# from langchain_google_genai import ChatGoogleGenerativeAI
# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash-preview-04-17",
#     temperature=0,
# )
