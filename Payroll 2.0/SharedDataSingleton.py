from square.client import Client
import os
from datetime import datetime

class SharedDataSingleton:

    """
            Description: Singleton class holds the shared 'Start Date', 'End Date', 'Restaurant Object', 'Client API'
            Parameters: 1.  startDate       (type: datetime)            ->          Start date of the payroll.
                        2.  endDate         (type: datetime)            ->          End date of the payroll.
                        3.  restaurant      (type: Restaurant)          ->          Restaurant object of which payroll is being generated.
                        4.  client          (type: Client)              ->          Client object for API calls.
    """

    __instance = None

    def __new__(cls, *args, **kwargs):
        
        if cls.__instance is None:
            cls.__instance = super(SharedDataSingleton,cls).__new__(cls)

        return cls.__instance

    def __init__(self, startDate, endDate, restaurant):
        
        self.startDate = startDate
        self.endDate = endDate
        self.restaurant = restaurant
        self.numberOfDays = (datetime.strptime(endDate, "%Y-%m-%dT%H:%M:%S%z")-datetime.strptime(startDate, "%Y-%m-%dT%H:%M:%S%z")).days
        self.client = Client(
            access_token=os.environ[f'{self.restaurant.production_access_token}'],
            environment='production')

    @classmethod
    def getInstance(cls):
        if cls.__instance == None:
            raise Exception ("The singleton object hasn't been instantiated yet.")

        else:
            return cls.__instance
