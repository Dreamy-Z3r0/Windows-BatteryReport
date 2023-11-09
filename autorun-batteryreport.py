import os
import datetime

from pathlib import Path

separator = '-'
extension = '.html'

baseCommand = "powercfg /batteryreport /output"

fileName = '\\'
fileDirectory = "D:\battery-report"

shellCommand = ''

# Generate file name accordingly to the date and time of report
def generate_fileName():
    global fileName     # Format: "YYYY-MM-DD HH-MM.html"

    # Extract datetime data
    current_datetime = datetime.datetime.now()

    # First field: year
    fileName += str(current_datetime.year) + separator

    # Second field: month
    temp = int(current_datetime.month)
    if (temp < 10):
        fileName += '0'
    fileName += str(temp) + separator

    # Third field: day
    temp = int(current_datetime.day)
    if (temp < 10):
        fileName += '0'
    fileName += str(temp) + ' '

    # Fourth field: hour
    temp = int(current_datetime.hour)
    if (temp < 10):
        fileName += '0'
    fileName += str(temp) + separator

    # Fifth field: minute
    temp = int(current_datetime.minute)
    if (temp < 10):
        fileName += '0'
    fileName += str(temp) + extension

#Generate shell command
def generate_shellCommand():
    global shellCommand    
    fileDirectory_full = fileDirectory + fileName
    shellCommand = baseCommand + ' ' + fileDirectory_full

def run_shellCommand():
    os.system(shellCommand)

generate_fileName()
generate_shellCommand()
run_shellCommand()
