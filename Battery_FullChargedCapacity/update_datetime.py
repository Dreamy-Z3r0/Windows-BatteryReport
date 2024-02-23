############################################
# Obtain date time data from an NTP server #
############################################

# Python package 'ntplib' to query NTP servers
package = 'ntplib'

# NTP server; all options are found on https://www.ntppool.org/zone/@
ntpServer = 'vn.pool.ntp.org'


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
    try:
        c = ntplib.NTPClient()
        response = c.request(ntpServer).tx_time
    except:
        controlFlag = 0
    
    if (0 == controlFlag):
        response = time()
    
    return strftime('%Y-%m-%d %H:%M:%S', localtime(response))


# Main function
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
        return fetch_datetime(installationResult)


if __name__ == "__main__":
    print(update_datetime())