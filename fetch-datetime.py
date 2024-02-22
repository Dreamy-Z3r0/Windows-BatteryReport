# Obtain date time data from an NTP server

package = 'ntplib'
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
    from time import ctime

    c = ntplib.NTPClient()
    response = c.request(ntp_server)
    output = ctime(response.tx_time)

    output = output.split(' ')

    output[0] = output[-1]
    del output[-1]

    if (1 == len(output[2])):
        output[2] = '0' + output[2]

    output = ' '.join(output)
    print(output)

def main():
    try:
        import ntplib
    except ImportError:
        print("No module named 'ntplib' found. Attempting to install...")

        result = install_missing()
        if (1 == result):
            result = 'success'
        else:
            result = 'failed'

        print(f'Installation message: {result}\n')
    finally:
        globals()[package] = __import__(package)
        fetch_datetime()

main()