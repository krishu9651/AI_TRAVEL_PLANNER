from tools.search_tool import web_search

def get_weather(destination):
    data = web_search(f"current weather in {destination}")
    return data