# Exam question about continue (try again) and break (stop the loop)
while True:
    try:
        number = int(input("enter a number: "))
        print(number)
        break
    except ValueError:
        print("Invalid number. Please try again.")
    except KeyboardInterrupt:
        print("You stopped the program.")
        break
    except Exception:
        print("An unexpected error occurred.")
        break