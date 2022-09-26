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
        """
        
        Description: Calls the necessary functions to get the tips and the 
        
        """
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
        
        tip_gratuity_dict = {}
        dates = []
        for order in orders_Json["orders"]:

            # GETTING THE DATE OF THE ORDER.
            date = order["created_at"]

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
            # print(date)

            if date not in dates:
                dates.append(date)

            
            # GETTING THE TIP MONEY
            tip_money = float((order["total_tip_money"]["amount"])/100)

            # GETTING THE AUTO GRATUITY FOR THE ORDER.
            auto_gratuity = float((order["total_service_charge_money"]["amount"])/100)

            if tip_gratuity_dict.get(date,None) == None:
                tip_gratuity_dict[date] = {
                    "tip":tip_money,
                    "auto gratuity":auto_gratuity
                }
            elif tip_gratuity_dict.get(date,None) != None:
                tip_gratuity = tip_gratuity_dict.get(date)
                tip_gratuity["tip"] += tip_money
                tip_gratuity["auto gratuity"] += auto_gratuity
                tip_gratuity_dict[date] = tip_gratuity

        print(tip_gratuity_dict)






