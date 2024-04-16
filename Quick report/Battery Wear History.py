# Generate a battery report
import os
import subprocess

outputFile = 'temp.html'
try:
    os.remove(outputFile)
except:
    pass

command = 'powercfg /batteryreport /output ' + outputFile
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)


# Read HTML contents of interest
contents = None
while True:
    try:
        with open(outputFile, 'r') as f:
            contents = f.read()
            f.close()
            os.remove('temp.html')
        del outputFile, command, process
        break
    except:
        pass

start = contents.find("Charge capacity history of the system's batteries")
stop = contents.rfind('mWh') + 3
contents = contents[start : stop]
contents = contents.replace('\n', '')
del start, stop


# Obtain data periods
periods = []
start = 0
lookupStr = '<td class="dateTime">'
maxLength = [0, 0]

while contents.find(lookupStr, start) > -1:
    start = contents.find(lookupStr, start) + len(lookupStr)
    stop = contents.find('</td>', start)
    value = contents[start : stop]
    while value.find('  ') > -1:
        value = value.replace('  ', ' ')
    periods.append(value)

    if len(value) > maxLength[0]:
        maxLength[0] = len(value)

del start, lookupStr


# Obtain the full-charged capacities
capacity = []
start = 0
index = 0
lookupStr = '<td class="mw">'

while contents.find(lookupStr, start) > -1:
    start = contents.find(lookupStr, start) + len(lookupStr)
    stop = contents.find(' mWh', start)
    value = contents[start : stop]

    if len(value) > maxLength[1]:
        maxLength[1] = len(value)

    value = int(value.replace(',', ''))
        
    if index % 2 == 0:
        capacity.append(value)
    else:
        temp = 1 - capacity[-1] / value
        capacity[-1] = (capacity[-1], temp)

    index += 1

del start, index, lookupStr, contents


# Print the result
tableHeader = ''
consolePrintContents = []

temp = 'Data period'
maxLengthHeader = maxLength[0]
if len(temp) > maxLengthHeader:
    maxLengthHeader = len(temp)

tableHeader += f'{temp:^{maxLengthHeader}}'
maxLengthHeader = [maxLengthHeader]

temp = "Full-charged Capacity"
maxLengthHeader.append(len(temp))
tableHeader += f' | {temp:^{maxLengthHeader[-1]}}'

temp = "Wear Level"
maxLengthHeader.append(len(temp))
tableHeader += f' | {temp:^{maxLengthHeader[-1]}}'

consolePrintContents.append(tableHeader)
consolePrintContents.append('-' * len(tableHeader))
del tableHeader

for i, _ in enumerate(periods):
    line = ''

    temp = f'{periods[i]:>{maxLength[0]}}'
    line += f'{temp:^{maxLengthHeader[0]}}'

    temp = f'{capacity[i][0]:{maxLength[1]},d} mWh'
    line += f' | {temp:^{maxLengthHeader[1]}}'

    temp = f'{capacity[i][1]:.2%}'
    line += f' | {temp:>{maxLengthHeader[2]}}'

    consolePrintContents.append(line)

for line in consolePrintContents:
    print(line)

while True:
    pass