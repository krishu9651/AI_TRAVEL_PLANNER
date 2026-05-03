# from models.llm_model import ask_gemini
# from tools.search_tool import web_search

# def research_agent(destination):
#     data = web_search(f"Travel tips, scams, best food, hidden gems in {destination}")

#     prompt = f'''
#     You are a travel researcher.

#     Destination: {destination}

#     Research Data:
#     {data}

#     Give practical travel insights, local tips, food suggestions, and hidden gems.
#     '''

#     return ask_gemini(prompt)

from tools.search_tool import web_search

def research_agent(destination):
    info = web_search(destination)
    return info