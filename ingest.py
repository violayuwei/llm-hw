import requests
from minsearch import Index
from gitsource import GithubRepositoryDataReader


def load_faq_data():
    reader = GithubRepositoryDataReader(
        repo_owner="DataTalksClub",
        repo_name="llm-zoomcamp",
        commit_id="8c1834d",
        allowed_extensions={"md"},
        filename_filter=lambda path: "/lessons/" in path,
    )

    documents = [file.parse() for file in reader.read()]
    
    return documents
    
    
    #url_prefix = 'https://datatalks.club/faq'

    # for course in courses_raw:
    #     course_url = f'{url_prefix}{course["path"]}'
    #     course_response = requests.get(course_url)
    #     course_response.raise_for_status()
    #     course_data = course_response.json()

    #     documents.extend(course_data)

    # for doc in documents:
    #     doc["doc_id"] = doc.pop("id") #we do this so we can add the id key to sqlite so we don't reimport the same records

    # return documents

def build_index(documents):
    index = Index(
        text_fields=['content'],
        keyword_fields=['filename']
    )
    index.fit(documents)
    return index
