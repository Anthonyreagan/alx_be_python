
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        message = f"{task} is a high priority task"
    case "medium":
        message = f"{task} is a medium priority task."
    case "low":
        message = f"{task} is a low priority task."
    case _:
        message = f"{task} priority level is yet unknown."

if time_bound == 'yes':
    message += "that requires immidiate attention today!"
    print("\nReminder:", message)

elif time_bound == 'no':
    message += " Concider completing it at your own free time"
    print("\nNote:", message)
