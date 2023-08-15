from dotenv import load_dotenv
load_dotenv()

import os
import openai

from langchain.chat_models import ChatOpenAI, AzureChatOpenAI, ChatGooglePalm

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage, BaseOutputParser

model = "gpt-4"
temperature = 0.7

openai_api_key = os.getenv("OPENAI_API_KEY")

azure_openai_key = os.getenv("AZURE_OPENAI_KEY")
azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

google_palm_key = os.getenv("GOOGLE_PALM_AI_API_KEY")

prompt: str = "Write an introductory paragraph to explain Generative AI to the reader of this content."
template = ("You are a helpful assistant that answers this question.")
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])


def openai_text_completion():
    openai.api_version = '2020-11-07'
    chat = ChatOpenAI(openai_api_key = openai_api_key,
		model = model,
		temperature = temperature)
    llm_response = chat(
        chat_prompt.format_prompt(
            text = prompt
        ).to_messages())

    return llm_response.content

def azureopenai_text_completion():
    chat = AzureChatOpenAI(openai_api_type = "azure",
                  openai_api_key = azure_openai_key,
                  openai_api_base = azure_openai_endpoint,
                  deployment_name = azure_openai_deployment_name,
                  model = model,
                  temperature = temperature,
                  openai_api_version = "2023-05-15")
    llm_response = chat(
	chat_prompt.format_prompt(
            text = prompt
        ).to_messages())

    return llm_response.content

def google_palm_text_completion():
   model = "models/text-bison-001"
   chat = ChatGooglePalm(
                  google_api_key = google_palm_key,
                  model = model,
                  temperature = temperature)
   llm_response = chat(
        chat_prompt.format_prompt(
            text = prompt
        ).to_messages())

   return llm_response.content

def main():
    response = openai_text_completion()
    print(response)
    response = azureopenai_text_completion()
    print(response)
    response = google_palm_text_completion()
    print(response)

if __name__ == '__main__':
    main()
