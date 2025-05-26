
description = input("Whats the task description?: ")
priority = input("Whats the task priority (high, medium or low)?: ")
time_bound = input("Is the task time-bound?(yes or no): ")

match priority:
    case "high":
        message = f"{description} is a high priority task"
    case "medium":
        message = f"{description} is a medium priority task."
    case "low":
        message = f"{description} is a low priority task."
    case _:
        message = f"{description} priority level is yet unknown."

if time_bound == 'yes':
    message += "that requires immidiate attention today!"
    print("\nReminder:", message)

elif time_bound == 'no':
    message += " Concider completing it at your own free time"
    print("\nNote:", message)
