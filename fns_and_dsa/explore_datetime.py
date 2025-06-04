import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    formated_date_time = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print(f"current date and time is: {formated_date_time}")

def calculate_future_date():
    current_date = datetime.datetime.now()
    number_of_days = int(input("Enter the number of days to add to the current date: ").strip().lower())
    future_date = current_date + timedelta(number_of_days)
    formated_future_date = future_date.strftime("%Y-%m-%d")

    print(f"date after {number_of_days} days will be: {formated_future_date}")
    

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()