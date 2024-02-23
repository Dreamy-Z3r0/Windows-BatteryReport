import Battery_FullChargedCapacity.update_fullChargedCapacity as update_fullChargedCapacity
import Battery_FullChargedCapacity.update_datetime as update_datetime
import handle_log

logContainer = '.'
logFilename = 'Monitor - Battery Full-charged Capacity.csv'

logFilename_fullpath = logContainer + '\\' + logFilename


def main_process():
    # Obtain timestamp
    timestamp = update_datetime.update_datetime().split(' ')

    # Obtain full-charged capacity
    fullChargedCapacity = update_fullChargedCapacity.update_fullChargedCapacity()

    # Create a data list
    newData = timestamp
    newData.append(str(fullChargedCapacity) + '\n')

    # Write to log file
    handle_log.file_write_field(logFilename_fullpath, newData)


if __name__ == '__main__':
    main_process()
