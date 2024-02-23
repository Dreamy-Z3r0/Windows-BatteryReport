import os


###############################
# Define types of log headers #
###############################

# Full-charged capacity log file
logHeaderRow_fullchargedCapacity = ['Date', 'Time', 'Full-charged Capacity\n']



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
def file_write_field(fileFullPath, listInput):
    try:
        # Analyse log filename
        logFilename = analyse_dir(fileFullPath)
        logFilename = logFilename[-1]

        if ('Monitor - Battery Full-charged Capacity.csv' == logFilename):
            logFilename = 1
        else:
            raise Exception(f"Error: Invalid log name: {logFilename}")

        if (isinstance(listInput, list)):
            if not(file_check(fileFullPath)):
                if (1 == logFilename):
                    file_write_field(fileFullPath, logHeaderRow_fullchargedCapacity)

            file_newLine = ','.join(listInput)
            f = open(fileFullPath, 'a')
            f.write(file_newLine)
            f.close()
        else:
            raise Exception(f"Error: Expected <class 'list'> input.\n\t'{listInput}' is of {type(listInput)}.")
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
