import sys
import datetime
from Restaurant import Restaurant
import OrderIdList as orders
from Payroll import Payroll
from pytz import timezone
import pytz
from Utility import Utility
from SharedDataSingleton import SharedDataSingleton


"""
python3 main.py Kricket 06-10-2022 06-10-2022

# sys.argv[1]           ------>         Restaurant name
# sys.argv[2]           ------>         start_date
# sys.argv[3]           ------>         end_date

"""

class Main:

    @staticmethod
    def main():

        if __name__ == "__main__":
            
            # FORMATTING THE START DATES 
            start_date, end_date = Utility.convertDateToRFC3339(sys.argv[2], sys.argv[3])
            
            # FIRST TIME CREATING A SHARED DATA SINGLETON OBJECT
            SharedDataSingleton(start_date, end_date,Restaurant( sys.argv[1]))
            
            payroll_obj = Payroll()

            payroll_obj.generatePayroll()


Main.main()