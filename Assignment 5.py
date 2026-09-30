# create a program that analyzes a series of personal expenses
#ask user repeatedly to enter expenses until they enter 0 to indicate they are done

# This Loops the program until the user enters 0 to indicate they are done entering expenses.
expenses = []
while True: 
    expense = float(input("Enter an expense (or 0 to finish): "))
    
    if expense == 0:
        break
    if expense < 0:
        print("expense cannot be a negative number")
    else:
        expenses.append(expense)
if len(expenses) == 0:
    print("No expenses were entered.")
else:
    small_count = 0
    moderate_count = 0
    large_count = 0

    for expense in expenses:
        if expense < 25:
            small_count += 1
        elif expense < 100:
            moderate_count += 1
        else:
            large_count += 1

    total = sum(expenses)
    average = total / len(expenses)
    smallest = min(expenses)
    largest = max(expenses)

#This tells python to print the results of the analysis in a clear and organized manner
    print()
    print("Expense summary")
    print(f"Number of expenses: {len(expenses)}")
    print(f"Total expenses: ${total:.2f}")
    print(f"Average expense: ${average:.2f}")
    print(f"Smallest expense: ${smallest:.2f}")
    print(f"Largest expense: ${largest:.2f}")
    print(f"Number of small expenses (<$25): {small_count}")
    print(f"Number of moderate expenses: {moderate_count}")
    print(f"Number of large expenses: {large_count}")