# TODOs
* Clearly break out examples where we have a 'solved' incident, right now I see a number of results which lacked a solved example in the prompt.  Perhaps use a different prompt when there is no solved incident available
* Explore generating rules from the LLM walking the diff between initial/solved branches and summarizing/iterating and look to discover common themes in files.
* Use structured data via [pydantic](https://docs.pydantic.dev/latest/) for our interaction with the LLM

# Notes related to learning and exploring this space

## Prompt Engineering
* https://platform.openai.com/docs/guides/prompt-engineering/six-strategies-for-getting-better-results

## NBDev
nbdev is a tool/approach for developing python code in jupyter notebooks and then exporting that to it's own files for later reuse.  We are experimenting with using it to aid prototyping by communicating to others our thinking process as we explore new libraries/code and capturing the interaction/output for later reading
    * https://nbdev.fast.ai/tutorials/tutorial.html

## GitPython
Using GitPython to interact with Git
* https://gitpython.readthedocs.io/en/stable/quickstart.html

## Langchain
Using langchain for our interaction with LLMs
* Short courses from DeepLearing.ai
    * [LangChain for LLM Application Development](https://learn.deeplearning.ai/langchain/lesson/1/introduction)
    * [LangChain Chat with Your Data](https://learn.deeplearning.ai/langchain-chat-with-your-data/lesson/1/introduction)
* Videos
    * [LangChain Crash Course: Build a AutoGPT app in 25 minutes!](https://www.youtube.com/watch?v=MlK6SIjcjE8)
* Tutorials/Examples
    * https://python.langchain.com/docs/expression_language/cookbook/code_writing
* Langchain Expression Language
    * https://github.com/pinecone-io/examples/blob/master/learn/generation/langchain/handbook/11-langchain-expression-language.ipynb  
        * Related YouTube: [LangChain Expression Language (LCEL) Explained!](https://www.youtube.com/watch?v=O0dUOtOIrfs)

## Agents
* https://agentprotocol.ai/
* https://github.com/Significant-Gravitas/AutoGPT


## Interesting Papers
* [ReAct: SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS(https://arxiv.org/pdf/2210.03629.pdf)
* [Repository-Level Prompt Generation for Large Language Models of Code](https://arxiv.org/abs/2206.12839v2)
* [CodePlan: Repository-level Coding using LLMs and Planning](https://arxiv.org/pdf/2309.12499.pdf)
* [Guiding Language Models of Code with Global Context using Monitors](https://arxiv.org/abs/2306.10763)
    * https://github.com/microsoft/monitors4codegen
    * Highlights: 
            Some recent approaches use static analysis (Shrivastava et al., 2022; Ding et al., 2022; Pei et al., 2023)
            or retrieval (Zhang et al., 2023) to extract relevant code fragments from the global context. These approaches expand the prompt (Shrivastava et al., 2022; Pei et al., 2023; Zhang et al., 2023) or require architecture modifications (Ding et al., 2022) and additional training (Ding et al., 2022; Pei et al.,
            2023). In comparison, we provide token-level guidance to a frozen LM by invoking static analysis on demand. Our method is complementary to these approaches as they condition the generation by modifying the input to the LM, whereas we apply output-side constraints by reshaping the logits.
* [RepoFusion: Training Code Models to Understand
Your Repository](https://arxiv.org/pdf/2306.10998.pdf)

## Interestig Blog Posts/Examples/Tutorials
* [ReAct: Synergizing Reasoning and Acting in Language Models](https://react-lm.github.io/)
* [CodePlan: Repository-level Coding using LLMs and Planning](https://arxiv.org/pdf/2309.12499.pdf)
* [Fine-Tune LLaMA 2 with QLoRA](https://colab.research.google.com/drive/1Zmaceu65d7w4Tcd-cfnZRb6k_Tcv2b8g?usp=sharing)
    * From: https://github.com/smol-ai/llama-fine-tuning-hackameetup/tree/main#getting-started
* [Codebase Analysis: Langchain Agents](https://carbonated-yacht-2c5.notion.site/Codebase-Analysis-Langchain-Agents-0b0587acd50647ca88aaae7cff5df1f2)


## Misc Tools/Libs/Frameworks
* https://streamlit.io/
    * "Streamlit turns data scripts into shareable web apps in minutes.
All in pure Python. No front‑end experience required."
* https://openrouter.ai/docs#models
* https://typer.tiangolo.com/
    * "Typer is a library for building CLI applications that users will love using and developers will love creating. Based on Python 3.6+ type hints"
* https://fastapi.tiangolo.com/python-types/

# Reference Projects to consult
* https://github.com/smol-ai/developer


