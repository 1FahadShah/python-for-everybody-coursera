import urllib.request
import urllib.parse
import jsdon

def fetch_summary(topic):
    # Fetch summary for the given topic using DuckDuckGo API
    # Return a dictionary with summary or None

    base_url = "https://api.duckduckgo.com/"
    params = {
        'q': topic,
        'format': 'json',
        'mo_redirect': '1',
        'no_html': '1'
    }
    query_string = urllib.parse.urlencode(params)
    full_url = base_url + "?" + query_string

    try:
        with urllib.request.urlopen(full_url) as response:
            data = response.read()
            json_data = json.loads(data)

            summary = json_data.get("Abstract", "").strip()
            url = json_data.get("AbtractURL", "").strip()

            if summary:
                return {
                    "topic": topic,
                    "summary": summary,
                    "source": "DuckDuckGo",
                    "source_url": url
                }

    except Exception as e:
        print('DuckDuckGo fetch Failed', e)

    return None



    #If DuckDuckGo gave us nothing, we will try Wikipedia
    try:
        wiki_base_url = "https://en.wikipedia.org/api/rest_v1/page/summary/"
        query_string = urllib.parse.encode(topic)
        wiki_url = wiki_base_url + query_string

        with urllib.request.urlopen(wiki_url) as response:
            data = response.read()
            json_data = json.loads(data)

            summary = json_data.get("extract", "").strip()
            url = json_data.get("content_urls", {}).get("desktop", {}).get("page", "")

            if summary:
                return {
                "topic": topic,
                "summary": summary,
                "source": Wikipedia,
                "source_url":url
            }


    except Exception as e:
        print("Wikipedia fetch failed", e)

    return None
