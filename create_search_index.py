import os
import json
import requests
import setupenv

setupenv.setup()

cognitive_search_name = os.getenv("AZURE_SEARCH_SERVICE_NAME")
index_name = os.getenv("AZURE_SEARCH_SERVICE_INDEX_NAME")
api_key = os.getenv("AZURE_SEARCH_SERVICE_ADMIN_KEY")
create_index_url = f"https://{cognitive_search_name}.search.windows.net/indexes/{index_name}?api-version=2023-07-01-Preview"
insert_entries_url = f"https://{cognitive_search_name}.search.windows.net/indexes/{index_name}/docs/index?api-version=2023-07-01-Preview"
search_url = f"https://{cognitive_search_name}.search.windows.net/indexes/{index_name}/docs/search?api-version=2023-07-01-Preview"

def create_index(embedding_length):
    payload = json.dumps({
        "name": index_name,
        "fields": [
            {
                "name": "id",
                "type": "Edm.String",
                "key": True,
                "filterable": True
            },
            {
                "name": "title",
                "type": "Edm.String",
                "searchable": True,
                "retrievable": True
            },
            {
                "name": "content",
                "type": "Edm.String",
                "searchable": True,
                "retrievable": True
            },
            {
                "name": "tag",
                "type": "Edm.String",
                "filterable": True,
                "searchable": True,
                "retrievable": True
            },
            {
                "name": "metadata",
                "type": "Edm.String",
                "filterable": True,
                "searchable": True,
                "retrievable": True
            },
            {
                "name": "content_vector",
                "type": "Collection(Edm.Single)",
                "searchable": True,
                "retrievable": True,
                "dimensions": embedding_length,
                "vectorSearchConfiguration": "my-vector-config"
            }
        ],
        "vectorSearch": {
            "algorithmConfigurations": [
                {
                    "name": "my-vector-config",
                    "kind": "hnsw",
                    "hnswParameters": {
                        "m": 4,
                        "efConstruction": 400,
                        "metric": "cosine"
                    }
                }
            ]
        },
        "semantic": {
            "configurations": [
                {
                    "name": "my-semantic-config",
                    "prioritizedFields": {
                        "titleField": {
                            "fieldName": "title"
                        },
                        "prioritizedContentFields": [
                            {
                                "fieldName": "content"
                            }
                        ],
                        "prioritizedKeywordsFields": [
                            {
                                "fieldName": "tag"
                            }
                        ]
                    }
                }
            ]
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'api-key': api_key
    }

    response = requests.request("PUT", create_index_url,
                                headers=headers, data=payload)
    print(response.content)
    return response.status_code

if __name__ == '__main__':
    result = create_index(1536)
    print(result)