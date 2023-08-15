# LLM Text Completion via langchain - A Simplified Demo

- clone this repo
- rename example.env to .env
- set environment variables in .env file
  - OPENAI_API_KEY from https://platform.openai.com/account/api-keys
  - Azure OpenAI Service Settings from Azure OpenAI https://portal.azure.com
    - AZURE_OPENAI_KEY 
    - AZURE_OPENAI_ENDPOINT
    - AZURE_OPENAI_DEPLOYMENT_NAME
  - GOOGLE_PALM_AI_API_KEY from https://makersuite.google.com
  - GOOGLE_PROJECT_ID from Google Cloud console
  - Add GCP Credential file as gcp-cred.json for Vertex AI
- for running individual Python programs, use this

  Installation 

      pip install -r requirements.txt
  
  OpenAI Python API, Azure OpenAI Service, PaLM API and Vertex AI
 
      python text-completion.py
  
or use these notebooks

- [Gradio App](https://nbviewer.org/github/amitpuri/LLM-Text-Completion-langchain/blob/main/gradio-app.ipynb)


Further, simplify using  Semantic Kernel
- [Text Completion via Semantic Kernel](https://github.com/amitpuri/LLM-Text-Completion-Semantic-Kernel)
- [Text Completion via OpenAI API Python](https://github.com/amitpuri/LLM-Text-Completion)
  
More comprehensive demos are available on [LLM Scenarios, Use cases on the Gradio app](https://github.com/amitpuri/ask-picturize-it)
