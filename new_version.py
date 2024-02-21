import subprocess

# Obtain battery full-charged capacity infomation
systeminfo = subprocess.run(["Powershell", "-NonInteractive", "-Command", "Get-WmiObject", "-Namespace",  "'root\wmi'", "-Query",  "'select FullChargedCapacity  from BatteryFullChargedCapacity'"], capture_output=True).stdout.decode().strip()

# Look for the line containing the battery full-charged capacity
data_field_index = systeminfo.index('FullChargedCapacity :')
end_of_data_line = systeminfo.index('\n', data_field_index)

# Slice string for data line
systeminfo = systeminfo[data_field_index : end_of_data_line]

# Obtain the data field index within the data line
data_field_index = systeminfo.index(':') + 2

# Slice data field for data
systeminfo = systeminfo[data_field_index:]

# Convert data from string to int
fullcharge_capacity = int(systeminfo)

# Print the obtained data
print(fullcharge_capacity)
