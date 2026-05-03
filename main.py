from teams.travel_team import run_travel_team

destination = input("Enter destination: ")
days = int(input("How many days?: "))

plan, pdf = run_travel_team(destination, days)

print("\n\n========= YOUR AI TRAVEL PLAN =========\n")
print(plan)
print(f"\nPDF Saved At: {pdf}")