import os

logFilename = './Battery-Capacity.csv'


def file_check():
    isExisting = os.path.isfile(logFilename)

    if (not(isExisting)):
        f = open(logFilename, 'x')
        f.close()

    return isExisting


if __name__ == '__main__':
    print(file_check())