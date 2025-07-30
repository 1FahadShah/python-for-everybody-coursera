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


    except Exception as e:
        print('DuckDuckGo fetch Failed', e)