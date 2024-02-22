import os

logFilename = './Battery-Capacity.csv'
logHeaderRow = ['Date', 'Time', 'Full-charged Capacity\n']


def file_check():
    isExisting = os.path.isfile(logFilename)

    if not(isExisting):
        f = open(logFilename, 'x')
        f.close()

    return isExisting


def file_write_field(listInput):
    if (isinstance(listInput, list)):
        if not(file_check()):
            file_write_field(logHeaderRow)

        file_newLine = ','.join(listInput)
        f = open(logFilename, 'a')
        f.write(file_newLine)
        f.close()
    else:
        print(f"Error: Expected <class 'list'> input.\n\t'{listInput}' is of {type(listInput)}.")


if __name__ == '__main__':
    file_write_field(['field 1', 'field 2', 'field 3\n'])
    file_write_field(['field 4', 'field 5', 'field 6\n'])
    file_write_field('This is a wrong input type')