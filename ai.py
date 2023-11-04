import openai
import os
openai.api_type = os.environ["OPENAI_API_TYPE"]
openai.api_version = os.environ["OPENAI_API_VERSION"]
openai.api_base = os.environ["OPENAI_API_BASE"]
openai.api_key =  os.environ["OPENAI_API_KEY"]

from datetime import datetime, timezone
last_time = datetime.now()

def get_agent_chain(memory):
    from langchain.chat_models import AzureChatOpenAI
    from langchain import LLMChain
    from langchain.agents import ZeroShotAgent, AgentExecutor

    import aitools
    tools = aitools.get_tools()

    prefix = """You are an anthropomorphic elephant. Your name is Emily. You are a personal assistant to a human. You were created by Cameron Vetter. You are witty and funny and sometimes snarky, and answer questions as best you can. When you do not know the answer to a question you will state that you don't know. You have access to the following tools:"""
    suffix = """Begin!"

    Previous conversation:
    {history}  
    Question: {input}
    {agent_scratchpad}"""

    prompt = ZeroShotAgent.create_prompt(
        tools, 
        prefix=prefix, 
        suffix=suffix, 
        input_variables=["history", "input", "agent_scratchpad"]
    )


    llm = AzureChatOpenAI(deployment_name="gpt4small", openai_api_version="2023-03-15-preview", temperature=0.5, client=None)
    llm_chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True, max_iterations=5, return_intermediate_steps=True)
    agent_chain = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True, memory=memory, handle_parsing_errors="Check your output and make sure it conforms!", return_intermediate_steps=True)
    return agent_chain

def get_response(agent_chain, prompt):
    global last_time
    last_time = datetime.now()
    reply = agent_chain({"input": prompt})
    return reply