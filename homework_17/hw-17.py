import random
from datetime import datetime, timedelta


def add_subtract_days(input_date, days, is_add):
    """
    Add or subtract days from date provided by user
    """
    if is_add:
        result_date = input_date + timedelta(days=days)
    else:
        result_date = input_date - timedelta(days=days)
    return result_date


def calculate_age(birth_date):
    """
    Calculate exact age as a timestamp
    """
    current_date = datetime.now()
    age = current_date - birth_date
    return current_date, age.total_seconds()


# Create a list comprehension of 100 elements in range from 1 to 10
random_numbers = [random.randint(1, 10) for _ in range(100)]
# Count each element
element_count = {i: random_numbers.count(i) for i in range(1, 11)}

custom_date = datetime(2023, 10, 20)
print("Add 5 days to a current date:", add_subtract_days(custom_date, 5, True))
print("Subtract 5 days from current date:", add_subtract_days(custom_date, 5, False))
print("Count age as timestamp:", calculate_age(datetime(1985, 10, 29)))
print("Count each element in list:", element_count)
