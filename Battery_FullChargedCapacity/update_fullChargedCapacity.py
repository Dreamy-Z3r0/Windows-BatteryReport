import subprocess


def update_fullChargedCapacity():
    # Obtain battery full-charged capacity infomation
    systeminfo = subprocess.run(["Powershell", "-NonInteractive", "-Command", "Get-WmiObject", "-Namespace",  "'root\\wmi'", "-Query",  "'select FullChargedCapacity  from BatteryFullChargedCapacity'"], capture_output=True).stdout.decode().strip()

    # Look for the line containing the battery full-charged capacity
    dataFieldIndex = systeminfo.index('FullChargedCapacity :')
    endOfDataLine = systeminfo.index('\n', dataFieldIndex)

    # Slice string for data line
    systeminfo = systeminfo[dataFieldIndex : endOfDataLine]

    # Obtain the data field index within the data line
    dataFieldIndex = systeminfo.index(':') + 2

    # Slice data field for data
    systeminfo = systeminfo[dataFieldIndex:]

    # Convert data from string to int
    fullChargedCapacity = int(systeminfo)

    # Return full charged capacity value
    return fullChargedCapacity


if __name__ == '__main__':
    print(update_fullChargedCapacity())