from square.client import Client
import os
import JsonParser as jp
import json
import pprint
import datetime
from pytz import timezone
import pytz

class Payroll:

    def __init__(self, restaurant, start_date, end_date):

        self.__start_date = start_date
        self.__end_date = end_date
        self.__restaurant = restaurant

        self.__client = Client(
            access_token=os.environ[f'{self.__restaurant.production_access_token}'],
            environment='production')

    def generatePayroll(self):

        order_list = self.__getListOfOrderIdFromPaymentAPI()
        orders_Json = self.__getOrdersFromOrdersAPI(order_list)
        self.__getGratuityAndTipsFromOrdersJson(orders_Json)




    def __getListOfOrderIdFromPaymentAPI(self):
        """
            Description: This function takes the restaurant name
        """

        result = self.__client.payments.list_payments(
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

    
    def __getOrdersFromOrdersAPI(self, order_list):

        result = self.__client.orders.batch_retrieve_orders(
        body = {
            "location_id": self.__restaurant.location_id,
            "order_ids": order_list
          }
        )

        if result.is_success():
            # print(result.body)
            with open("orderAPI.json", "w") as outfile:
                json.dump(result.body, outfile, indent = 4)
            return result.body

        elif result.is_error():
            print(result.errors)

    
    def __getGratuityAndTipsFromOrdersJson(self, orders_Json):
        
        dates = []
        for order in orders_Json["orders"]:
            date = order["closed_at"]
            date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fz")
            pst_tz = timezone('US/Pacific')
            pacific_now = datetime.datetime.now(pst_tz)
            offset = -1 * (pacific_now.utcoffset().total_seconds()/60/60)
            date = date - datetime.timedelta(hours=offset)
            date = date.strftime("%Y-%m-%d")

            # date = pst_tz.normalize(date.astimezone(pst_tz))
            if date not in dates:
                dates.append(date)

        print(dates)





