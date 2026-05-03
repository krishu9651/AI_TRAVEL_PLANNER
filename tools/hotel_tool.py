from tools.search_tool import web_search

def hotel_suggestions(destination):
    data = web_search(f"best budget hotels in {destination}")
    return data