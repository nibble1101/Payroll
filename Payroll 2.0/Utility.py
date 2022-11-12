import sys
import datetime
from Restaurant import Restaurant
import OrderIdList as orders
from pytz import timezone
import pytz

class Utility:

    @staticmethod
    def convertDateToRFC3339(start_date, end_date):

        start_date, end_date = start_date.split('-'), end_date.split('-')
        start_month, start_day, start_year = int(start_date[0]), int(start_date[1]), int(start_date[2])
        end_month, end_day, end_year = int(end_date[0]), int(end_date[1]), int(end_date[2])

        start_date = datetime.datetime(start_year, start_month, start_day, 0, 0)
        end_date = datetime.datetime(end_year, end_month, end_day, 23, 59)
        
        utc_start_date = start_date.astimezone(datetime.timezone.utc)
        utc_end_date = end_date.astimezone(datetime.timezone.utc)

        start_date = utc_start_date.isoformat()
        end_date = utc_end_date.isoformat()

        print(f'Start Date: {type(start_date)}')
        print(f'End Date: {end_date}')

        print(f'UTC Start Date: {type(utc_start_date)}')
        print(f'UTC End Date: {utc_end_date}')

        

        return start_date, end_date

    @staticmethod
    def convertUTCDateToPST(date):

        # FIXING THE DATE FROM UTC TO PST
        try:
            date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fz")
        except ValueError:
            date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%Sz")
        pst_tz = timezone('US/Pacific')
        pacific_now = datetime.datetime.now(pst_tz)
        offset = -1 * (pacific_now.utcoffset().total_seconds()/60/60)
        date = date - datetime.timedelta(hours=offset)
        date = date.strftime("%Y-%m-%d")

        return date
