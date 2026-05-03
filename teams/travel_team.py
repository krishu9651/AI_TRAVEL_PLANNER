from agents.research_agent import research_agent
from agents.planner_agent import planner_agent
from tools.weather_tool import get_weather
from tools.hotel_tool import hotel_suggestions
from tools.budget_tool import estimate_budget
from tools.pdf_tool import generate_pdf

def run_travel_team(destination, days):
    research = research_agent(destination)
    weather = get_weather(destination)
    hotels = hotel_suggestions(destination)
    budget = estimate_budget(days)

    final_plan = planner_agent(destination, days, budget, research, weather, hotels)

    pdf_file = generate_pdf(final_plan)

    return final_plan, pdf_file