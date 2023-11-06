import os

def setup():
    os.environ["OPENAI_API_KEY"] = ''

    os.environ["SERPAPI_API_KEY"] = ''
    os.environ["GPLACES_API_KEY"] = ''

    os.environ["AZURE_SEARCH_SERVICE_NAME"] = ''
    os.environ["AZURE_SEARCH_SERVICE_INDEX_NAME"] = ''
    os.environ["AZURE_SEARCH_SERVICE_ADMIN_KEY"] = ''