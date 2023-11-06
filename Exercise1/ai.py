from datetime import datetime, timezone
last_time = datetime.now()

def get_agent_chain():
    from langchain.chat_models import ChatOpenAI
    from langchain import LLMChain
    from langchain.agents import ZeroShotAgent, AgentExecutor

    prefix = """You are a chat bot."""
    suffix = """Begin!"

    Question: {input}"""

    prompt = ZeroShotAgent.create_prompt(
        prefix=prefix, 
        suffix=suffix, 
        input_variables=["history", "input", "agent_scratchpad"]
    )


    llm = ChatOpenAI(model_name="gpt-4-0613", temperature=0.5, client=None)
    llm_chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    agent = ZeroShotAgent(llm_chain=llm_chain, verbose=True, max_iterations=5, return_intermediate_steps=True)
    agent_chain = AgentExecutor.from_agent_and_tools(agent=agent, verbose=True, handle_parsing_errors="Check your output and make sure it conforms!", return_intermediate_steps=True)
    return agent_chain

def get_response(agent_chain, prompt):
    global last_time
    last_time = datetime.now()
    reply = agent_chain({"input": prompt})
    return reply