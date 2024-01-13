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
# https://bam.res.ibm.com/docs/api-reference#text-generation
# decoding_method refers to 
# Represents the strategy used for picking the tokens during generation of the output text.
# Options are greedy and sample. Value defaults to sample if not specified.
# https://huggingface.co/blog/how-to-generate

# max_new_tokens seems to need to be under 1536 tokens
params = GenerateParams(decoding_method="sample", max_new_tokens=1536)

# Instantiate a model proxy object to send your requests
granit = Model("ibm/granite-20b-code-instruct-v1", params=params, credentials=creds)

prompts = [
    """ Write a Quarkus program that returns the current time from a REST
        API
    """
          ]
for response in granit.generate(prompts):
    print(response.generated_text)
