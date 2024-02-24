import subprocess

unit = 'mWh/h'

def operation_mode():
    # Obtain availability of AC power line
    systeminfo = subprocess.run(["Powershell", "-NonInteractive", "-Command", "Get-WmiObject -Namespace root\\wmi -Class BatteryStatus | select 'PowerOnline'"], capture_output=True).stdout.decode().strip()

    # Separate data lines
    systeminfo = systeminfo.split('\n')

    # Fetch info line
    operationMode = systeminfo[-1]
    index_effectiveData = 0
    try:
        index_effectiveData = operationMode.index('True')
        operationMode = ["On AC"]
    except:
        index_effectiveData = operationMode.index('False')
        operationMode = ["On battery"]

    # Update charge rate (mWh/h)
    chargeRate_value = chargeRate()
    operationMode.append(chargeRate_value)

    # Update discharge rate (mWh/h)
    dischargeRate_value = dischargeRate()
    operationMode.append(dischargeRate_value)

    # Insert warnings (if any)
    warning = "No warning"
    condition1 = not(chargeRate_value == ('+0' + unit))
    condition2 = not(dischargeRate_value == ('-0' + unit))
    if (condition1 & condition2):
        warning = "Issue with charging condition."
        operationMode.append(warning)

    condition1 = "On AC" == operationMode[0]
    condition2 = not(dischargeRate_value == ('-0' + unit))
    if (condition1 & condition2):
        warning = "Plugged in, not charging"
        operationMode.append(warning)

    if ("No warning" == warning):
        operationMode.append(warning)

    return operationMode

# Charge rate
def chargeRate():
    systeminfo = subprocess.run(["Powershell", "-NonInteractive", "-Command", "Get-WmiObject -Namespace root\\wmi -Class BatteryStatus | select 'ChargeRate'"], capture_output=True).stdout.decode().strip()

    # Separate data lines
    systeminfo = systeminfo.split('\n')

    # Fetch info line
    output = systeminfo[-1]
    output = int(output)

    # Convert back to string
    output = '+' + str(output) + unit

    return output

# Discharge rate
def dischargeRate():
    systeminfo = subprocess.run(["Powershell", "-NonInteractive", "-Command", "Get-WmiObject -Namespace root\\wmi -Class BatteryStatus | select 'DischargeRate'"], capture_output=True).stdout.decode().strip()

    # Separate data lines
    systeminfo = systeminfo.split('\n')

    # Fetch info line
    output = systeminfo[-1]
    output = int(output)

    # Convert back to string
    output = '-' + str(output) + unit

    return output

# Charge rate / Discharge rate as int
def rateValue(rateInput):
    startPos = 1
    endPos = rateInput.index('mWh/h')
    rateInput = rateInput[startPos:endPos]
    return int(rateInput)

# Battery voltage
def update_voltage():
    # Obtain battery voltage
    systeminfo = subprocess.run(["Powershell", "-NonInteractive", "-Command", "Get-WmiObject -Namespace root\\wmi -Class BatteryStatus | select 'Voltage'"], capture_output=True).stdout.decode().strip()

    # Separate data lines
    systeminfo = systeminfo.split('\n')

    # Fetch info line
    voltage = systeminfo[-1]
    
    # Data conversion: string to float
    voltage = format(float(voltage) / 1000, '.2f')

    # Return battery voltage
    return voltage

# Remaining capacity
def remaining_capacity(fullChargedCapacity):
    # Obtain remaining capacity
    systeminfo = subprocess.run(["Powershell", "-NonInteractive", "-Command", "Get-WmiObject -Namespace root\\wmi -Class BatteryStatus | select 'RemainingCapacity'"], capture_output=True).stdout.decode().strip()

    # Separate data lines
    systeminfo = systeminfo.split('\n')

    # Fetch info line
    remainingCapacity = int(systeminfo[-1])

    # Return remaining capacity percentage
    return format((remainingCapacity / fullChargedCapacity * 100), '.1f')


if __name__ == '__main__':
    print(f'Mode of operation: {operation_mode()}')
    print(f'Battery voltage: {update_voltage()} V')