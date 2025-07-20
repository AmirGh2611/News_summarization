from http.client import HTTPSConnection
from urllib.parse import urlencode
from transformers import pipeline
from MyToken import my_token
import pandas as pd
import json


def ui(text, search_field, categories, number):
    connection = HTTPSConnection("api.thenewsapi.com")
    params = urlencode({
        "api_token": my_token,
        "search": text,
        "search_field": search_field,
        "categories": categories,
        "limit": number
    })
    connection.request("GET", f"/v1/news/all?{params}")

    res = connection.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)
    summarizer = pipeline("summarization")
    results = []
    for i in data["data"]:
        title = i["title"]
        url = i["url"]
        description = i["description"]
        summary = summarizer(description, max_length=56, min_length=25, do_sample=False)[0]["summary_text"]
        results.append({
            "Title": title,
            "Summary": summary,
            "URL": url
        })
    df = pd.DataFrame(results)
    return df
