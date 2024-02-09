class Outing:
    COACH_HIRE_COSTS = {"12-16": 150, "17-26": 190, "27-39": 225}
    MEAL_COSTS = {"12-16": 14.00, "17-26": 13.50, "27-39": 13.00}
    THEATRE_TICKET_COSTS = {"12-16": 21.00, "17-26": 20.00, "27-39": 19.00}
    MIN_SENIORS_REQUIRED = 10
    MAX_SENIORS_ALLOWED = 36
    MIN_CARERS = 2

    def __init__(self, num_people):
        self.num_people = num_people

    def calculate_cost(self):
        if self.num_people < self.MIN_SENIORS_REQUIRED or self.num_people > self.MAX_SENIORS_ALLOWED:
            return "Outing cannot proceed. Number of seniors must be between 10 and 36."
        group = "12-16" if self.num_people <= 16 else "17-26" if self.num_people <= 26 else "27-39"
        coach_cost = self.COACH_HIRE_COSTS[group]
        meal_cost_per_person = self.MEAL_COSTS[group]
        ticket_cost_per_person = self.THEATRE_TICKET_COSTS[group]
        total_cost = coach_cost + (meal_cost_per_person + ticket_cost_per_person) * self.num_people
        return total_cost, total_cost / self.num_people if self.num_people else 0

class OutingDetails:
    def __init__(self, outing):
        self.outing = outing
        self.outing_details = []

    def record(self):
        for i in range(self.outing.num_people):
            name = input(f"Enter the name of senior citizen {i+1}: ")
            payment = float(input(f"Enter the amount paid by {name}: $"))
            self.outing_details.append((name, payment))
        for i in range(self.outing.MIN_CARERS):
            name = input(f"Enter the name of carer {i+1}: ")
            self.outing_details.append((name, 0))
        return self.outing_details

# Test the program
def main():
    num_seniors = int(input("Enter the number of senior citizens interested in the outing: "))
    outing = Outing(num_seniors)
    total_cost, cost_per_person = outing.calculate_cost()
    if isinstance(total_cost, str):
        print(total_cost)
    else:
        print(f"Total cost for the outing: ${total_cost:.2f}")
        print(f"Cost per person for senior citizens: ${cost_per_person:.2f}")

        outing_details = OutingDetails(outing)
        outing_records = outing_details.record()

        print("\nOuting Details:")
        total_collected = 0
        for name, payment in outing_records:
            total_collected += payment
            print(f"Name: {name}, Amount Paid: ${payment:.2f}")

        print(f"\nTotal amount collected: ${total_collected:.2f}")

if __name__ == "__main__":
    main()
