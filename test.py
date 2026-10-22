has_error = True

while has_error:
	try:
		number = int(input("Enter a number: "))
		print(number)
	except ValueError:
		print("Invalid number. Please try again.")
		continue
	else:
		has_error = False
	finally:
		print("Got through it!")