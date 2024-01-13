#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from genai.credentials import Credentials
from genai.model import Model
from genai.schemas import GenerateParams

# make sure you have a .env file under ibm-generative-ai root with
# GENAI_KEY=<your-genai-key>
# GENAI_API=<genai-api-endpoint>
load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
api_url = os.getenv("GENAI_API", None)
creds = Credentials(api_key, api_endpoint=api_url) # credentials object to access the LLM service

# Instantiate parameters for text generation
params = GenerateParams(decoding_method="sample", max_new_tokens=10)

# Instantiate a model proxy object to send your requests
flan_ul2 = Model("google/flan-ul2", params=params, credentials=creds)

prompts = ["Hello! How are you?", "How's the weather?"]
for response in flan_ul2.generate(prompts):
    print(response.generated_text)
