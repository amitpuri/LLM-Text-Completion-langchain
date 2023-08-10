# LLM Text Completion - A Simplified Demo

- clone this repo
- rename example.env to .env
- set environment variables in .env file
  - OPENAI_API_KEY from https://platform.openai.com/account/api-keys
  - Azure OpenAI Service Settings from Azure OpenAI https://portal.azure.com
    - AZURE_OPENAI_KEY 
    - AZURE_OPENAI_ENDPOINT
    - AZURE_OPENAI_DEPLOYMENT_NAME
  - GOOGLE_PALM_AI_API_KEY from https://makersuite.google.com
- for running individual Python programs, use this

  Installation 

      pip install -r requirements.txt
  
  OpenAI Python API & Azure OpenAI Service
 
      python text-completion.py
  
or use these notebooks

- [Gradio App](https://nbviewer.org/github/amitpuri/LLM-Text-Completion-langchain/blob/main/gradio-app.ipynb)

More comprehensive demo available on https://github.com/amitpuri/ask-picturize-it
