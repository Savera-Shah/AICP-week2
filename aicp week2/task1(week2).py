# Constants for cost calculation
COACH_HIRE_COSTS = {
    "12-16": 150,
    "17-26": 190,
    "27-39": 225
}

MEAL_COSTS = {
    "12-16": 14.00,
    "17-26": 13.50,
    "27-39": 13.00
}

THEATRE_TICKET_COSTS = {
    "12-16": 21.00,
    "17-26": 20.00,
    "27-39": 19.00
}

MIN_SENIORS_REQUIRED = 10
MAX_SENIORS_ALLOWED = 36
MIN_CARERS = 2
ADDITIONAL_CARER_THRESHOLD = 24

def calculate_cost(num_people):
    if num_people < MIN_SENIORS_REQUIRED or num_people > MAX_SENIORS_ALLOWED:
        return "Outing cannot proceed. Number of seniors must be between 10 and 36."
    
    # Determine coach hire cost based on number of people
    if num_people <= 16:
        coach_cost = COACH_HIRE_COSTS["12-16"]
    elif num_people <= 26:
        coach_cost = COACH_HIRE_COSTS["17-26"]
    else:
        coach_cost = COACH_HIRE_COSTS["27-39"]
    
    # Calculate meal cost per person
    if num_people <= 16:
        meal_cost_per_person = MEAL_COSTS["12-16"]
    elif num_people <= 26:
        meal_cost_per_person = MEAL_COSTS["17-26"]
    else:
        meal_cost_per_person = MEAL_COSTS["27-39"]
    
    # Calculate theatre ticket cost per person
    if num_people <= 16:
        ticket_cost_per_person = THEATRE_TICKET_COSTS["12-16"]
    elif num_people <= 26:
        ticket_cost_per_person = THEATRE_TICKET_COSTS["17-26"]
    else:
        ticket_cost_per_person = THEATRE_TICKET_COSTS["27-39"]
    
    # Calculate total cost
    total_cost = coach_cost + (meal_cost_per_person + ticket_cost_per_person) * num_people
    
    # Calculate cost per person for seniors
    cost_per_person = total_cost / num_people
    
    return total_cost, cost_per_person

# Test the program
num_seniors = int(input("Enter the number of senior citizens interested in the outing: "))

total_cost, cost_per_person = calculate_cost(num_seniors)

if isinstance(total_cost, str):
    print(total_cost)
else:
    print(f"Total cost for the outing: ${total_cost:.2f}")
    print(f"Cost per person for senior citizens: ${cost_per_person:.2f}")
