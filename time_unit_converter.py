# This script converts minutes to hours and minutes, and seconds to hours, minutes, and seconds.

# Convert minutes to hours and minutes
course_minutes = float(input("Please enter the number of minutes:\n"))
hours = int(course_minutes // 60)  # Use int() to ensure hours is an integer
minutes = int(course_minutes % 60)  # Use int() to ensure minutes is an integer
message = f"This course is {hours} hours and {minutes} minutes."
print(message)

# Convert seconds to hours, minutes, and seconds
total_seconds = int(input("Please enter the number of seconds:\n"))
minutes = total_seconds // 60
remaining_seconds = total_seconds % 60
hours = minutes // 60
remaining_minutes = minutes % 60
message = f"{hours} hours, {remaining_minutes} minutes, {remaining_seconds} seconds."
print(message)