
from math import ceil
from datetime import datetime, timedelta


def calculate_parking_fee(park_time, pickup_time):
    park_time = datetime.strptime(park_time, "%H:%M")
    pickup_time = datetime.strptime(pickup_time, "%H:%M")

    add_extra = pickup_time < park_time

    if add_extra:
        pickup_time += timedelta(days=1)  # Adjust pickup time to the next day if it's before park time
    # Calculate the total parking time in hours
    total_time = (pickup_time - park_time).total_seconds() / 3600
    round_total_time = abs(ceil(total_time))  # Round up to the nearest hour
    # Define the parking fee structure
    if round_total_time == 1:
        fee = 5  # Flat fee for the first hour
    elif round_total_time > 1:
        fee = round_total_time * 3  # $3 for each additional hour after the first
    
    if add_extra:
        fee += 10  # Add an extra $10 if pickup time is before park time

    return f"${fee}"

# Example usage:
#print(calculate_parking_fee("08:00", "10:30"))  # Output: $11
print(calculate_parking_fee("18:15", "01:30"))  # Output: $18