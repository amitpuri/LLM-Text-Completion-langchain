from dotenv import load_dotenv
load_dotenv()

import os
import openai
from langchain.chat_models import ChatOpenAI, AzureChatOpenAI

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage, BaseOutputParser

#model = "gpt-35-turbo"
model = "gpt-4"
temperature = 0.7
azure_openai_key = os.getenv("AZURE_OPENAI_KEY")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_api_base = f"https://{azure_endpoint}.openai.azure.com"
azure_openai_deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

prompt: str = "Write an introductory paragraph to explain Generative AI to the reader of this content." 
template = ("You are a helpful assistant that answers this question.")
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])


chat = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"),model=model,temperature=temperature)

llm_response = chat(
    chat_prompt.format_prompt(
        text=prompt
    ).to_messages()
)

print(llm_response.content)

chat = AzureChatOpenAI(openai_api_type = "azure",
                  openai_api_key = azure_openai_key,
                  openai_api_base = azure_openai_api_base,
                  deployment_name = azure_openai_deployment_name,
                  model = model,
                  temperature = temperature, 
                  openai_api_version="2023-05-15")


llm_response = chat(
    chat_prompt.format_prompt(
        text=prompt
    ).to_messages()
)

print(llm_response.content)