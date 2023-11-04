import os

def setup():
    os.environ["OPENAI_API_TYPE"] = 'azure'
    os.environ["OPENAI_API_VERSION"] = '2022-12-01'
    os.environ["OPENAI_API_BASE"] = 'https://<YOURINSTANCE>.openai.azure.com/'
    os.environ["OPENAI_API_KEY"] = '<YOURKEY>'

    os.environ["SERPAPI_API_KEY"] = '<YOURKEY>'
    os.environ["GPLACES_API_KEY"] = '<YOURKEY>'

    os.environ["AZURE_SEARCH_SERVICE_NAME"] = '<YOURSEARCHNAME>'
    os.environ["AZURE_SEARCH_SERVICE_INDEX_NAME"] = '<YOURINDEXNAME>'
    os.environ["AZURE_SEARCH_SERVICE_ADMIN_KEY"] = '<YOURKEY>'