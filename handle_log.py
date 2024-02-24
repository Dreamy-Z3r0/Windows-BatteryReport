import os


###############################
# Define types of log headers #
###############################

# Battery information log file
logHeaderRow_batteryInformation = {
    'date': 'Date',
    'time': 'Time',
    'unique id': 'Battery Unique ID',
    'voltage': 'Battery Voltage (V)',
    'mode of operation': 'Mode of Operation',
    'charge rate': 'Charge Rate (mWh/h)',
    'discharge rate': 'Discharge Rate (mWh/h)',
    'designed capacity': 'Designed Capacity (mWh)',
    'full-charged capacity': 'Full-charged Capacity (mWh)',
    'remaining capacity': 'Remaining Capacity (%)',
    'battery health': 'Battery Health (%)'
}



############################
# Define package functions #
############################

# Get directory components
def analyse_dir(fileFullPath):
    container = [0, 0]
    try:
        container = fileFullPath.split('\\')
    except:
        print(f"{fileFullPath} is not a valid directory.")
    finally:
        return container


# Check if log file exists
def file_check(fileFullPath):
    isExisting = os.path.isfile(fileFullPath)
    if not(isExisting):
        # Obtain the directory part
        logContainer = analyse_dir(fileFullPath)
        del logContainer[-1]
        logContainer = '\\'.join(logContainer)      

        # Check if the folder for the log is the working directory
        if not('.' == logContainer):
            print(logContainer)
            # Create the folder if it does not exist
            if not(os.path.isdir(logContainer)):
                os.makedirs(logContainer)
                print("Here")

        # Create the log file if it does not exist
        f = open(fileFullPath, 'x')
        f.close()

    return isExisting


# Main function: write to file
def file_write_field(fileFullPath, dictInput):
    try:
        # Analyse log filename
        logFilename = analyse_dir(fileFullPath)
        logFilename = logFilename[-1]

        if ('Monitor - Battery Information.csv' == logFilename):
            logFilename = 1
        else:
            raise Exception(f"Error: Invalid log name: {logFilename}")

        if (isinstance(dictInput, dict)):
            if not(file_check(fileFullPath)):
                if (1 == logFilename):
                    file_write_field(fileFullPath, logHeaderRow_batteryInformation)

            file_newLine = []
            if (1 == logFilename):
                file_newLine.append(dictInput['date'])
                file_newLine.append(dictInput['time'])
                file_newLine.append(dictInput['unique id'])
                file_newLine.append(str(dictInput['designed capacity']))
                file_newLine.append(str(dictInput['voltage']))
                file_newLine.append(dictInput['mode of operation'])
                file_newLine.append(str(dictInput['charge rate']))
                file_newLine.append(str(dictInput['discharge rate']))
                file_newLine.append(str(dictInput['full-charged capacity']))
                file_newLine.append(str(dictInput['remaining capacity']))
                file_newLine.append(str(dictInput['battery health']) + '\n')

            file_newLine = ','.join(file_newLine)
            f = open(fileFullPath, 'a')
            f.write(file_newLine)
            f.close()
        else:
            raise Exception(f"Error: Expected <class 'dict'> input.\n\t'{dictInput}' is of {type(dictInput)}.")
    except Exception as error_msg:
        print(error_msg)



#########################
# Independent unit test #
#########################

if __name__ == '__main__':
    logContainer = '.'
    logFilename = 'Monitor - Battery Full-charged Capacity.csv'

    logFilename_fullpath = logContainer + '\\' + logFilename

    file_write_field(logFilename_fullpath, ['field 1', 'field 2', 'field 3\n'])
    file_write_field(logFilename_fullpath + 'meh', ['field 4', 'field 5', 'field 6\n'])
    file_write_field(logFilename_fullpath, 'This is a wrong input type')
    file_write_field(logFilename_fullpath, ['field 4', 'field 5', 'field 6\n'])
