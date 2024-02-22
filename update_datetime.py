############################################
# Obtain date time data from an NTP server #
############################################

# Python package 'ntplib' to query NTP servers
package = 'ntplib'

# NTP server; all options are found on https://www.ntppool.org/zone/@
ntpServer = 'vn.pool.ntp.org'

# Output datetime
outputDatetime = 0

# Attempt to install the ntplib module if it's missing
def install_missing():
    outputCode = 1
    try:
        import os
        os.system('pip install ntplib')
    except:
        outputCode = 0
    finally:
        return outputCode

# Fetch datetime data from NTP server
def fetch_datetime(controlFlag):
    from time import time, strftime, localtime

    response = 0

    if (controlFlag):
        c = ntplib.NTPClient()
        response = c.request(ntpServer).tx_time
    else:
        response = time()
    
    output = strftime('%Y-%m-%d %H:%M:%S', localtime(response))
    return output

def update_datetime():
    installationResult = 1
    try:
        __import__(package)
    except ImportError:
        # Attempt to install missing 'ntplib' package
        installationResult = install_missing()
    finally:
        if (installationResult):
            globals()[package] = __import__(package)
        outputDatetime = fetch_datetime(installationResult)
        print(outputDatetime)


if __name__ == "__main__":
    update_datetime()