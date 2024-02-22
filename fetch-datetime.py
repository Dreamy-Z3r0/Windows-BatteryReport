############################################
# Obtain date time data from an NTP server #
############################################

# Python package 'ntplib' to query NTP servers
package = 'ntplib'

# NTP server; all options are found on https://www.ntppool.org/zone/@
ntp_server = 'vn.pool.ntp.org'

# Attempt to install the ntplib module if it's missing
def install_missing():
    output_code = 1
    try:
        import os
        os.system('pip install ntplib')
    except:
        output_code = 0
    finally:
        return output_code

# Fetch date - time data
def fetch_datetime():
    from time import strftime, localtime

    c = ntplib.NTPClient()
    response = c.request(ntp_server)
    output = strftime('%Y-%m-%d %H:%M:%S', localtime(response.tx_time))
    print(output)

def main():
    installation_result = 1
    try:
        __import__(package)
    except ImportError:
        # Attempt to install missing 'ntplib' package
        installation_result = install_missing()
        
    finally:
        print(f'Installation message: {installation_result}\n')
        globals()[package] = __import__(package)
        fetch_datetime()

main()