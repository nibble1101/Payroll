from square.client import Client
import os
import JsonParser as jp

class Payroll:

    def __init__(self, restaurant, start_date, end_date):

        self.__start_date = start_date
        self.__end_date = end_date
        self.__restaurant = restaurant

    def getListOfOrderId(self):
        """
            Description: This function takes the restaurant name
        """
        client = Client(
            access_token=os.environ[f'{self.__restaurant.production_access_token}'],
            environment='production')

        result = client.payments.list_payments(
            begin_time = self.__start_date,
            end_time = self.__end_date,
            location_id = self.__restaurant.location_id
        )

        if result.is_success():
            # pprint.pprint(result.body)
            json_dict_object = result.body
            return jp.extractOrderList(json_dict_object)
        elif result.is_error():
            print(result.errors)