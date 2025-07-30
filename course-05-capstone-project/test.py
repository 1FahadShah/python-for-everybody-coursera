from crawler.fetch import fetch_summary

topic = "Machine Learning"

result = fetch_summary(topic)

if result:
    print("fetch successful\n")
    print("Topic: ", result["topic"])
    print("Source: ", result["source"])
    print("URL: ", result["source_url"])
    print("Summary: ", result["summary"])
else:
    print("Fetch failed")