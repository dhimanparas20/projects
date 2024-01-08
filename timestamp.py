from datetime import datetime

# Current date and time
current_datetime = datetime.now()

# Combine date and time components into a single string
combined_datetime = current_datetime.strftime("%Y%m%d%H%M%S")

print("Combined Date and Time:", combined_datetime)
