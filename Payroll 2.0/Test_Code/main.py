import sys
from restaurant import Restaurant
from payroll import Payroll
from Utility import Utility
from SharedDataSingleton import SharedDataSingleton


"""
python3 main.py Kricket 07-04-2022 07-18-2022

# sys.argv[1]           ------>         Restaurant name
# sys.argv[2]           ------>         start_date
# sys.argv[3]           ------>         end_date

"""

class Main:

    @staticmethod
    def main():

        if __name__ == "__main__":
            
            # FORMATTING THE START DATE AND END DATE
            start_date, end_date = Utility.convertDateToRFC3339(sys.argv[2], sys.argv[3])
            # start_date, end_date = Utility.convertDateToRFC3339('07-04-2022', '07-18-2022')
            
            # FIRST TIME CREATING A SHARED DATA SINGLETON OBJECT
            obj = SharedDataSingleton(start_date, end_date,Restaurant(sys.argv[1]))
            obj.pacificStartDate = sys.argv[2]
            obj.pacificEndDate = sys.argv[3]
            # SharedDataSingleton(start_date, end_date,Restaurant('Kricket'))
            
            payroll_obj = Payroll()

            payroll_obj.generatePayroll()


Main.main()