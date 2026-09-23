# Road trip planner
# IS 303 - level 2 assignment
# This program estimates cost of a round-trip road trip


print("====================")
print("Road Trip Planner")
print("====================") 

# Get info from people
User_name = input("What is your name?")
destination = input("Where are you traveling?")
one_way_miles = float(input("How many miles is the trip one way?"))
miles_per_gallon = float(input("What is you vehicle's miles per gallon?"))
gas_price = float(input("What is the gas price per gallon?"))
travelers = int(input("How mant travelers are going?"))

# Trip info
total_miles = one_way_miles * 2 
gallons_needed = total_miles / miles_per_gallon
gas_cost = gallons_needed * gas_price
cost_per_traveler = gas_cost / travelers

#Summary of Trip
print("===========================")
print("Trip Summary")
print("===========================")
print(f"Traveler: {User_name.upper()}")
print(f"Destination: {destination}")
print(f"Total Miles: {total_miles}")
print(f"Gallons of Gas: {gallons_needed:.2f}")
print(f"Gas Cost: ${gas_cost:.2f}")
print(f"Cost per Traveler: ${cost_per_traveler:.2f}")
print("===========================")
print("Have a great trip!")