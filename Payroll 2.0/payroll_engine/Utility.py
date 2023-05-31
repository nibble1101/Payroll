import sys
import datetime
from pytz import timezone

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

        print(f'Start Date: {start_date}')
        print(f'End Date: {end_date}')

        print(f'UTC Start Date: {utc_start_date}')
        print(f'UTC End Date: {utc_end_date}')

        

        return start_date, end_date

    @staticmethod
    def convertUTCDateToPST(date):

        # FIXING THE DATE FROM UTC TO PST
        try:
            date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fz")
        except ValueError:
            try:
                date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%Sz")

            except ValueError:
                date = datetime.datetime.fromisoformat(date)

        pst_tz = timezone('US/Pacific')
        pacific_now = datetime.datetime.now(pst_tz)
        offset = -1 * (pacific_now.utcoffset().total_seconds()/60/60)
        date = date - datetime.timedelta(hours=offset)
        date = date.strftime("%Y-%m-%d")

        return date

    @staticmethod
    def getHours(start, end):

        # 2022-07-17T18:02:21-07:00

        start = datetime.datetime.fromisoformat(start)
        end = datetime.datetime.fromisoformat(end)

        # print(start, end)

        difference = end - start

        # Calculate the number of hours in the difference
        hours = difference.total_seconds() / 3600

        return round(hours, 2)
        

# Utility.getHours("2022-07-17T18:02:00-07:00", "2022-07-17T21:21:00-07:00")