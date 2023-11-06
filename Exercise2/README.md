# Introduction 
This repo is part of a Workshop and may not be very useful if you are not currently in that workshop!

# Prepping VS Code
1. Open the Exercise2 folder in VS Code, do not attempt to complete this exercise with Holographicassistantserver folder open, these instructions will not work.
2. Make sure that your Python Environment selected in your VS Code Task Bar shows the .VENV python environment created previously. (This is only visible if a python file is currently open.)
   
![image](https://github.com/CameronVetter/HolographicAssistantServer/blob/main/images/venv.png?raw=true)

3. You will have to navigate to python.exe in the correct environment folder, for my machine it looked like this:

![image](https://github.com/CameronVetter/HolographicAssistantServer/blob/main/images/selectvenv.png?raw=true)

# Part 1
1. Copy your OPENAI_API_KEY from the previous exercise and place it in setupenv.py
2. Lets get our first tool working.  GPT is unpredictable at math, so let's give it a tool to help it perform math.
3. Run the flask server and open the swagger ui: http://127.0.0.1:5000/swagger/
4. Open ai.py, replace the line `tools = []` with this code:

```
    import aitools
    tools = aitools.get_tools()
```

5. Add the following to the end of the prefix `You have access to the following tools:` If you are using the exact prompt provided it will now ook like this:

```
    prefix = """You are an anthropomorphic elephant. Your name is Emily. You are a personal assistant to a human. You were created by Cameron Vetter. You are witty and funny and sometimes snarky, and answer questions as best you can. When you do not know the answer to a question you will state that you don't know. You have access to the following tools:"""
```

6. Run the flask server and open the swagger ui: http://127.0.0.1:5000/swagger/
7. Try the "Post Chat" method, and send the message "What is 1000 * 1234 + 50?"  Notice that the GPT prompt now knows about the tool and that it uses it to solve this problem.
8. Try a much more complicated math problem "What is the square root of 300?"  Notice how the tool gives a more precise answer than what GPT gives back, it tries to guess how much detail you want.
9. Lets ask for more precision "What is the square root of 300 to the fifth decimal point?"  Most likely it tries to execute some python code, Well at least it tried...  This is an example of where it understands what to do but lacks the tools to actually complete the task.  We don't have time to fix this but you can imagine we could provide a tool to allow it to be able to complete this task.

# Part 2
1. Lets turn this thing loose on the internet.
2. Open aitools.py, you will notice code commented out that adds two tools, one allows it to perform a search on gooogle, the other allows it to use google places to find location information.  Uncomment this code.
3. Open setup.env, and add keys for SERPAPI_API_KEY and GPLACES_API_KEY.
4. The SERPAPI_API_KEY is created at: https://serpapi.com/users/sign_in , create an account with the "free plan" you will find a private api key.
5. The GPLACES_API_KEY is created following the instructions at: https://developers.google.com/maps/documentation/places/web-service/get-api-key 
6. Run the flask server and open the swagger ui: http://127.0.0.1:5000/swagger/ 
7. Ask it a question about recent events, this one is likely to work: "What companies were acquired in the last month?"
8. Ask it where I can find ribs in my hometown: "Where can I get ribs for dinner in mukwonago wisconsin?" (The best places for Ribs in my town are David Alan Alan's and Boneyard)
9. Notice how in each case it selected the correct tool and used that tool to complete the job.  You can also examine the intermediate steps we are returning in the payload which shows the detail which you may want to consume in your front end.

# Part 3 
1. Now lets give this a Memory, open ai.py
2. Change the method `get_agent_chain`  to take a parameter called `memory`
3. Add a parameter in the `agent_chain` creation that is `memory=memory` 
4. We also need to change the prompt to make it use the memory. The function should look something like this now:

```
def get_agent_chain(memory):
    from langchain.chat_models import ChatOpenAI
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
        tools=tools,
        prefix=prefix, 
        suffix=suffix, 
        input_variables=["history", "input", "agent_scratchpad"]
    )


    llm = ChatOpenAI(model_name="gpt-4-0613", temperature=0.5, client=None)
    llm_chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True, max_iterations=5, return_intermediate_steps=True)
    agent_chain = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, memory=memory, verbose=True, handle_parsing_errors="Check your output and make sure it conforms!", return_intermediate_steps=True)
    return agent_chain
```

4. Open app.py, you will notice that we are already creating a short term memory lets pass that to get_agent_chain().  Line 10 should now look this:

```
agent_chain = ai.get_agent_chain(memory)
```

5. Run the flask server and open the swagger ui: http://127.0.0.1:5000/swagger/ 
6. Ask it the name of one of your family members.  I asked "What is my daughters name?"  It explains that it does not know the answer.
7. Tell it the name of that family member.  I said "My daughters name is Alexandria."
8. Now ask GPT for the name again.  I asked "What is my daughters name?"
9. Success!  Take a close look at the debug window and see how GPT used the memory to answer the question.
