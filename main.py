import meraki
import datetime
import pandas as pd

# Enter your API key

API_KEY = ''

dashboard = meraki.DashboardAPI(API_KEY)

# Network ID is necessary for this API endpoint

network_id = ''

# This function is used to manipulate time into ISO format

def updateTime():

    today = datetime.datetime.now().replace(microsecond=0)
    new_date = pd.to_datetime(today) + pd.DateOffset(days=7)
    as_string = str(new_date)
    dt = as_string.split()
    date = dt[0]
    time = dt[1]
    real_time = f'{date}T{time}Z'

    dashboard.networks.updateNetworkFirmwareUpgrades(
        network_id,
        products={'switch': {'nextUpgrade': {'time': real_time }}}
    )

def main():
    updateTime()

if __name__ == '__main__':
    main()
