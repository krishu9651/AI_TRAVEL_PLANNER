from models.llm_model import ask_gemini

def planner_agent(destination, days, budget, research, weather, hotels):
    prompt = f'''
    You are an expert AI Travel Planner.

    Destination: {destination}
    Days: {days}
    Budget: {budget}

    Research Info:
    {research}

    Weather Info:
    {weather}

    Hotel Info:
    {hotels}

    Create a complete day-wise smart travel itinerary with budget advice.
    '''

    return ask_gemini(prompt)