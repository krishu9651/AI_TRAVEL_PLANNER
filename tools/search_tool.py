# from ddgs import DDGS

# def web_search(query):
#     results_text = ""

#     with DDGS() as ddgs:
#         results = ddgs.text(query, max_results=5)

#         for r in results:
#             results_text += f"{r['title']} - {r['body']}\n"

#     return results_text


from ddgs import DDGS

def web_search(query):
    if not query:
        return "No query provided"

    results_text = ""

    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=5)

            for r in results:
                results_text += f"{r['title']} - {r['body']}\n"

        return results_text

    except Exception as e:
        return f"Search error: {str(e)}"