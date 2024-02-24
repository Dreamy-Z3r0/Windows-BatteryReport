import subprocess

# Battery unique ID
def fetch_UniqueID():
    # Obtain battery unique ID infomation
    systeminfo = subprocess.run(["Powershell", "-NonInteractive", "-Command", "Get-WmiObject -Namespace root\\wmi -Class BatteryStaticData | select 'UniqueID'"], capture_output=True).stdout.decode().strip()

    # Separate data lines
    systeminfo = systeminfo.split('\n')

    # Fetch unique ID line
    uniqueID = systeminfo[-1]

    # Return battery unique ID
    return uniqueID

# Designed capacity
def fetch_DesignedCapacity():
    # Obtain battery full-charged capacity infomation
    systeminfo = subprocess.run(["Powershell", "-NonInteractive", "-Command", "Get-WmiObject -Namespace root\\wmi -Class BatteryStaticData | select 'DesignedCapacity'"], capture_output=True).stdout.decode().strip()

    # Separate data lines
    systeminfo = systeminfo.split('\n')

    # Convert data from string to int
    designedCapacity = int(systeminfo[-1])

    # Return designed capacity value
    return designedCapacity


if __name__ == '__main__':
    print(f'Battery unique ID: {fetch_UniqueID()}')
    print(f'Designed capacity: {fetch_DesignedCapacity()}')