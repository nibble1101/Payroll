import sys
import datetime
from restaurant import Restaurant
import OrderIdList as orders
from payroll import Payroll
from pytz import timezone
import pytz

"""
python3 main.py Kricket 06-10-2022 06-10-2022

"""


if __name__ == "__main__":

    restaurant = sys.argv[1]
    start_date = sys.argv[2]
    end_date = sys.argv[3]

    start_date, end_date = start_date.split('-'), end_date.split('-')
    start_month, start_day, start_year = int(start_date[0]), int(start_date[1]), int(start_date[2])
    end_month, end_day, end_year = int(end_date[0]), int(end_date[1]), int(end_date[2])

    start_date = datetime.datetime(start_year, start_month, start_day, 0, 0)
    end_date = datetime.datetime(end_year, end_month, end_day, 23, 59)
    
    utc_start_date = start_date.astimezone(datetime.timezone.utc)
    utc_end_date = end_date.astimezone(datetime.timezone.utc)

    start_date = utc_start_date.isoformat()
    end_date = utc_end_date.isoformat()

    print(f'Start Date: {utc_start_date}')
    print(f'End Date: {utc_end_date}')

    restaurant_obj = Restaurant(restaurant)

    payroll_obj = Payroll(restaurant_obj, start_date, end_date)

    payroll_obj.generatePayroll()