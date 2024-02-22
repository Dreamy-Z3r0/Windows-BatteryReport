# Obtain date time data from an NTP server

ntp_server = 'vn.pool.ntp.org'

# Attempt to install the ntplib module if it's missing
def install_missing():
    import os
    
    try:
        os.system('pip install ntplib')
    except:
        return 0
    
    return 1

# Fetch date - time data
def fetch_datetime():
    from time import ctime

    c = ntplib.NTPClient()
    response = c.request(ntp_server)
    output = ctime(response.tx_time)

    print(f'Date-time: {output}')

def main():
    try:
        import ntplib
        fetch_datetime()
    except:
        print("No module named 'ntplib' found. Attempting to install...")

        result = install_missing()
        if (1 == result):
            result = 'success'
        else:
            result = 'failed'

        print(f'Installation message: {result}\n')

main()