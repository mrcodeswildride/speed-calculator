print()

distance = float(input("Enter the distance in miles: "))
total_time = float(input("Enter the time in hours: "))
hours_stop = float(input("How many hours to stop? "))

travel_time = total_time - hours_stop
speed = distance / travel_time

print(f"\nThe speed is {speed} miles per hour.")
