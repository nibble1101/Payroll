import sys
import datetime
from pytz import timezone
import pytz

"""
python3 main.py Kricket 06-10-2022 06-10-2022

"""


if __name__ == "__main__":

    start_date = "2022-06-11T02:49:36Z"

    date = datetime.datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%Sz")
    

    pst_tz = timezone('US/Pacific')

    pacific_now = datetime.datetime.now(pst_tz)
    offset = -1 * (pacific_now.utcoffset().total_seconds()/60/60)

    print(offset)
    date = date - datetime.timedelta(hours=offset)

    print(date.strftime("%Y-%m-%d"))