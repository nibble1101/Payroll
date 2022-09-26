from square.client import Client
import os

class sharedDataSingleton:

    """
            Description: Singleton class holds the shared 'Start Date', 'End Date', 'Restaurant Object', 'Client API'
            Parameters: 1.  startDate       (type: datetime)            ->          Start date of the payroll.
                        2.  endDate         (type: datetime)            ->          End date of the payroll.
                        3.  restaurant      (type: Restaurant)          ->          Restaurant object of which payroll is being generated.
    """

    __instance = None

    def __new__(cls, *args, **kwargs):
        
        if cls.__instance is None:
            cls.__instance = super(sharedDataSingleton,cls).__new__(cls)

        return cls.__instance

    def __init__(self, startDate, endDate, restaurant):
        
        self.startDate = startDate
        self.endDate = endDate
        self.restaurant = restaurant
        self.client = Client(
            access_token=os.environ[f'{self.restaurant.production_access_token}'],
            environment='production')

    @classmethod
    def getInstance(cls):
        if cls.__instance == None:
            raise Exception ("The singleton object hasn't been instantiated yet.")

        else:
            return cls.__instance
