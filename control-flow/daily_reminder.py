# Loop to ensure the script keeps running until valid input is given
while True:
    # Prompt for a Single Task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    # Process the Task Based on Priority using Match Case
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority. Please enter high, medium, or low.\n")
            continue  # Restart loop for correct input

    # Use if statement to modify reminder if time-bound
    if time_bound == "yes":
        print(f"Reminder: {reminder} that requires immediate attention today!")
    elif time_bound == "no":
        print(f"Note: {Reminder}. Consider completing it when you have free time.")
    else:
        print("Invalid input for time sensitivity. Please enter yes or no.\n")
        continue  # Restart loop for correct input

    break  # Exit loop once valid input is processed
