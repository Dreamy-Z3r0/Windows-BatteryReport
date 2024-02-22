import update_fullChargedCapacity
import update_datetime


# Print timestamp
timestamp = update_datetime.update_datetime().split(' ')
print(timestamp)

# Print the obtained data
fullChargedCapacity = update_fullChargedCapacity.update_fullChargedCapacity()
print(fullChargedCapacity)