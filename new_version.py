import update_fullChargedCapacity
import update_datetime
import handle_log


# Obtain timestamp
timestamp = update_datetime.update_datetime().split(' ')

# Obtain full-charged capacity
fullChargedCapacity = update_fullChargedCapacity.update_fullChargedCapacity()

# Create a data list
newData = timestamp
newData.append(str(fullChargedCapacity) + '\n')

# Write to log file
handle_log.file_write_field(newData)