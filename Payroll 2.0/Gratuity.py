from OrderJsonObj import OrderJsonObj
import datetime
from pytz import timezone
import pytz
from Utility import Utility

class Gratuity:

    def __init__(self, orders_Json_list):
        self.orders_Json_list = orders_Json_list
        self.dateGratuityDic = self.__generateDateGratuityDic()

    def __generateDateGratuityDic(self):
        dates = []
        dateGratuityDic = {}

        testGratuity = 0.0

        for orders_Json in  self.orders_Json_list:
            for order in orders_Json["orders"]:

                # GETTING THE DATE OF THE ORDER.
                date = order["created_at"]

                # FIXING THE DATE FROM UTC TO PST
                date = Utility.convertUTCDateToPST(date)

                if date not in dates:
                    dates.append(date)

                # THERE CAN BE MULTIPLE SERVICE CHARGES LIKE COURIER TIP, COUNTER TIP ETC. WE'RE ONLY INTERESTED IN
                # THE AUTO-GRATUITY.
                # GETTING THE LIST OF THE APPLIED SERVICE CHARGES.

                try:
                    service_charge_list = order["service_charges"]
                
                except KeyError:
                    continue
                
                gratuity_money = 0.0
                
                for service_charge in service_charge_list:
                    
                    if service_charge["type"] == "AUTO_GRATUITY":
                        # GETTING THE GRATUITY MONEY
                        gratuity_money += float((service_charge["applied_money"]["amount"])/100)

                if dateGratuityDic.get(date,None) == None:
                    dateGratuityDic[date] = {
                        "gratuity":gratuity_money
                    }

                elif dateGratuityDic.get(date,None) != None:
                    gratuity = dateGratuityDic.get(date)
                    gratuity["gratuity"] += gratuity_money
                    dateGratuityDic[date] = gratuity

        return dateGratuityDic

    