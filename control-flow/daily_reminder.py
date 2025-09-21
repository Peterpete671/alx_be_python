#Loop to allow retry if input is invalid
while True:   #Prompt for task details
	task = input("Enter your task: ")
	priority = input("Priority (high/medium/low): ").lower()
	time_bound = input("Is it time bound? (yes/no): ").lower()

	#Process task with match-case
	match priority:
		case "high":
			reminder = f" '{task}' is a high priority task"
		case "medium":
			reminder = f" '{task}' is a medium priority task"
		case "low":
			reminder = f" '{task}' is a low priority task"
		case _:
			print("Invalid priority. Please enter high, medium or low.\n")
			continue

	#Modify reminder if task is time-bound
	if time_bound == "yes":
		reminder += " that requires immediate attention today!"
	elif time_bound == "no":
		reminder += ". Consider completing it when you have free time."
	else:
		print("Invalid input for time sensitivity. Please enter yes or no.\n")
		continue
	#Final output
	print(f"\nReminder: {reminder}\n")
	break
