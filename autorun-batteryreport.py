import os

separator = '-'
extension = '.html'

baseCommand = "powercfg /batteryreport /output "

fileName = ''
subfolder = ''
fileDirectory = "D:\\battery-report"

reportContainer = ''
shellCommand = ''


# Generate file name accordingly to the date and time of report
def generate_fileName():
    import datetime
    global fileName, subfolder     # Format: "\YYYY-MM-DD HH-MM.html"

    # Extract datetime data
    current_datetime = datetime.datetime.now()

    # First field: year
    fileName = '\\' + str(current_datetime.year) + separator

    # Second field: month
    temp = int(current_datetime.month)
    if (temp < 10):
        fileName += '0'
    fileName += str(temp) + separator

    # Third field: day
    temp = int(current_datetime.day)
    if (temp < 10):
        fileName += '0'
    fileName += str(temp)

    subfolder = fileName

    # Fourth field: hour
    temp = int(current_datetime.hour)
    if (temp < 10):
        fileName += '0'
    fileName += ' ' + str(temp) + separator

    # Fifth field: minute
    temp = int(current_datetime.minute)
    if (temp < 10):
        fileName += '0'
    fileName += str(temp) + extension

#Generate shell command
def generate_shellCommand():
    global shellCommand, reportContainer

    # Generate the directory of the subfolder containing the battery report
    reportContainer = fileDirectory + subfolder

    # Generate the full shell command 
    report_fullPath = ' "' + reportContainer + fileName + '"'
    shellCommand = baseCommand + report_fullPath

# Make sure the folder containing the report exists
def create_container():
    from pathlib import Path

    container = Path(reportContainer)
    if not container.is_dir():
        os.system('mkdir ' + reportContainer)

# Generate battery report
def generate_report():
    create_container()
    os.system(shellCommand)

generate_fileName()
generate_shellCommand()


print(fileName)
print(shellCommand)

generate_report()
