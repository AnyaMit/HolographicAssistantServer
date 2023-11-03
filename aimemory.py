from langchain.memory import ConversationBufferMemory

def get_memory_redis():
    from langchain.memory.chat_message_histories import RedisChatMessageHistory

    # new plan https://python.langchain.com/en/latest/modules/memory/types/vectorstore_retriever_memory.html
    message_history = RedisChatMessageHistory(url='rediss://default:pZEuvvnUeompKkjUwGB4mY0zruhiaHjH8AzCaEItBLQ=@reddis-assistant.redis.cache.windows.net:6380', session_id='my-session')
    memory = ConversationBufferMemory(memory_key="chat_history", chat_memory=message_history, output_key="output", input_key="input", return_messages=True)
    return memory

# Secret install was:
# pip install --index-url=https://pkgs.dev.azure.com/azure-sdk/public/_packaging/azure-sdk-for-python/pypi/simple/ azure-search-documents==11.4.0a20230509004
from langchain.vectorstores.azuresearch import AzureSearch
from langchain.memory import VectorStoreRetrieverMemory

def get_vectorstore_azureSearch():

    vector_store = get_vector_store()
    
    retriever = vector_store.as_retriever(search_kwargs=dict(k=1))
    memory = VectorStoreRetrieverMemory(retriever=retriever, input_key="input")
    
    return memory

from typing import List
from langchain.docstore.document import Document

def create_memory_azureSearch(memory: List[Document]):
    from langchain.document_loaders import TextLoader
    from langchain.text_splitter import CharacterTextSplitter
    # loader = TextLoader('../../../state_of_the_union.txt')

    # documents = loader.load()
    # text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    # docs = text_splitter.split_documents(documents)
    vector_store = get_vector_store()

    return vector_store.add_documents(documents=memory)

def get_combined_memory( memory_redis: ConversationBufferMemory, memory_azure: VectorStoreRetrieverMemory):
    from langchain.memory import CombinedMemory

    memory = CombinedMemory(memories=[memory_redis, memory_azure])
    return memory

def get_vector_store():
    import os
    cognitive_search_name = os.environ["AZURE_SEARCH_SERVICE_NAME"]
    vector_store_address: str = f"https://{cognitive_search_name}.search.windows.net/"
    index_name: str = os.environ["AZURE_SEARCH_SERVICE_INDEX_NAME"]
    vector_store_password: str = os.environ["AZURE_SEARCH_SERVICE_ADMIN_KEY"]

    from langchain.embeddings.openai import OpenAIEmbeddings
    
    embeddings: OpenAIEmbeddings = OpenAIEmbeddings(model="text-embedding-ada-002", chunk_size=1, client=any)  
    vector_store: AzureSearch = AzureSearch(azure_cognitive_search_name=vector_store_address,  
                                        azure_cognitive_search_key=vector_store_password,  
                                        index_name=index_name,  
                                        embedding_function=embeddings.embed_query)  
    
    return vector_store