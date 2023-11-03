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
    Current conversation:
    {chat_history}    
    Question: {input}
    {agent_scratchpad}"""

    prompt = ZeroShotAgent.create_prompt(
        tools, 
        prefix=prefix, 
        suffix=suffix, 
        input_variables=["history", "input", "chat_history", "agent_scratchpad"]
    )


    llm = AzureChatOpenAI(deployment_name="gpt4small", openai_api_version="2023-03-15-preview", temperature=0.5, client=None)
    llm_chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True, max_iterations=5, return_intermediate_steps=True)
    agent_chain = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True, memory=memory, return_intermediate_steps=True)
    return agent_chain

def get_response(agent_chain, prompt):
    global last_time
    last_time = datetime.now()
    reply = agent_chain({"input": prompt})
    return reply

from langchain.memory import ConversationBufferMemory
from langchain.schema import BaseChatMessageHistory
def dream(memory: ConversationBufferMemory) -> bool:
    global last_time
    difference = (datetime.now() - last_time).total_seconds()
    print (difference)
    
    # if (difference > (10)):
    #     if (len(memory.chat_memory.messages) > 0):
    #         #there is chat history and no activiy for 10 minutes
    #         # if (create_long_term_memory(memory.chat_memory)):
    #         #     last_time = datetime.now()
    #         #     memory.chat_memory.clear()
    #         #     return True
    
    return False

# from langchain.schema import messages_to_dict, BaseMessage
# def create_long_term_memory(message_history: BaseChatMessageHistory) -> bool:
#     messages = messages_to_dict(message_history.messages)

#     memory = format_messages(messages)
#     analysis = analyze_conversation(memory)
#     subject = get_subject(analysis)
#     summary = get_summary(analysis)
#     subject_embeddings = generate_embeddings(subject)
#     memory_embeddings = generate_embeddings(memory)
#     id = create_id()

#     record = get_dict(id, memory, subject, summary, subject_embeddings, memory_embeddings)
#     json = get_json(record)

#     result1 = write_to_blob_storage(json, id)
#     result2 = save_to_vectordb(record)
#     return result1 and result2

# def format_messages(messages):
#     formatted_messages = []
#     for message in messages:
#         formatted_messages.append(f"{message['type']}: {message['data']['content']}")
#     return "\n".join(formatted_messages)

# from tenacity import retry, wait_random_exponential, stop_after_attempt

# @retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
# def analyze_conversation(memory):
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=f"What i the subject and a summary of the following conversation:\n\n{memory}\n",
#         temperature=0.3,
#         max_tokens=50,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0,
#         best_of=1,
#         stop=None)
#     return response.choices[0]['text']

# @retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
# # Function to generate embeddings for title and content fields
# def generate_embeddings(text):
#     response = openai.Embedding.create(input=text, engine="text-embedding-ada-002")
#     embeddings = response['data'][0]['embedding']
#     return embeddings

# def get_subject(analysis):
#     start_index = analysis.find("Subject: ") + len("Subject: ")
#     end_index = analysis.find("\nSummary:")
#     return analysis[start_index:end_index].strip()

# def get_summary(analysis):
#     start_index = analysis.find("Summary: ") + len("Summary: ")
#     return analysis[start_index:].strip()

# def get_dict(id: str, memory, subject, summary, subject_embeddings, memory_embeddings) -> dict:
#     return {'id': id,
#             'memory': memory,
#             'subject': subject,
#             'summary': summary,
#             'subjectVector': subject_embeddings,
#             'memoryVector': memory_embeddings}

# def get_json(dict) -> str:
#     import json
#     return json.dumps(dict)

# from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# def write_to_blob_storage(blob_data: str, id: str) -> bool:
#     import json
#     account_name = os.environ["blob_account_name"]
#     account_key = os.environ["blob_account_key"]
#     container_name = os.environ["blob_container_name"]
#     blob_name = f"{id}.json"

#     try:
#         # Create a BlobServiceClient object
#         blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

#         # Create a ContainerClient object
#         container_client = blob_service_client.get_container_client(container_name)

#         # Create a BlobClient object
#         blob_client = container_client.get_blob_client(blob_name)

#         # Upload blob data to Azure Blob Storage
#         blob_client.upload_blob(blob_data, overwrite=True)

#         return True
#     except Exception as e:
#         print(e)
#         return False

# import aimemory
# def save_to_vectordb(data) -> bool:
#     result = aimemory.create_memory_azureSearch(data)

#     return result.count == 1

# def create_id():
#     return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")