import BatteryInformation.update_fullChargedCapacity as update_fullChargedCapacity
import BatteryInformation.fetch_staticInformation as fetch_staticInformation
import BatteryInformation.update_status as update_status
import update_datetime
import handle_log

logContainer = '.'
logFilename = 'Monitor - Battery Information.csv'

logFilename_fullpath = logContainer + '\\' + logFilename


def main_process():
    # Create a data dictionary
    newData = {}

    # Obtain timestamp
    dataEntry = update_datetime.update_datetime().split(' ')
    newData.update({'date': dataEntry[0]})
    newData.update({'time': dataEntry[1]})

    # Obtain full-charged capacity
    dataEntry = update_fullChargedCapacity.update_fullChargedCapacity()
    newData.update({'full-charged capacity': dataEntry})

    # Obtain remaining capacity
    dataEntry = update_status.remaining_capacity(dataEntry)
    newData.update({'remaining capacity': dataEntry})

    # Obtain designed capacity
    dataEntry = fetch_staticInformation.fetch_DesignedCapacity()
    newData.update({'designed capacity': dataEntry})

    # Obtain battery voltage
    dataEntry = update_status.update_voltage()
    newData.update({'voltage': dataEntry})

    # Obtain mode of operation
    dataEntry = update_status.operation_mode()
    newData.update({'mode of operation': dataEntry[0]})

    # Obtain charge rate
    entryOfInterest = update_status.rateValue(dataEntry[1])
    newData.update({'charge rate': entryOfInterest})

    # Obtain discharge rate
    entryOfInterest = update_status.rateValue(dataEntry[2])
    newData.update({'discharge rate': entryOfInterest})

    # Assess battery health
    dataEntry = update_fullChargedCapacity.remaining_batteryHealth(newData['designed capacity'], newData['full-charged capacity'])
    newData.update({'battery health': dataEntry})

    # Obtain battery unique ID
    dataEntry = fetch_staticInformation.fetch_UniqueID()
    newData.update({'unique id': dataEntry})

    # Write to log file
    handle_log.file_write_field(logFilename_fullpath, newData)


if __name__ == '__main__':
    main_process()
