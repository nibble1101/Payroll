import sys
import datetime
from square.client import Client
import os
import pprint
import json



"""
        Description: Singleton class holds the shared 'Start Date', 'End Date', 'Restaurant Object', 'Client API'
        Parameters: 1.  startDate       (type: datetime)            ->          Start date of the payroll.
                    2.  endDate         (type: datetime)            ->          End date of the payroll.
                    3.  restaurant      (type: Restaurant)          ->          Restaurant object of which payroll is being generated.
"""