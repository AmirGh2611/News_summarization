from http.client import HTTPSConnection
from urllib.parse import urlencode
from transformers import pipeline
from MyToken import my_token


def ui(text, search_field, categories, language, number):
    connection = HTTPSConnection("api.thenewsapi.com")
    params = urlencode({
        "api_token": my_token,
        "search": text,
        "search_field": search_field,
        "categories": categories,
        "language": language,
        "limit": number
    })
    connection.request("GET", f"/v1/news/all?{params}")

    res = connection.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    summarizer = pipeline("summarization")
