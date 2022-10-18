from OrderJsonObj import OrderJsonObj
import datetime
from pytz import timezone
import pytz

class Gratuity:

    def __init__(self, orders_Json_list):
        self.orders_Json_list = orders_Json_list
        self.dateGratuityDic = self.__generateDateGratuityDic()

    def __generateDateGratuityDic(self):
        
        dates = []
        dateGratuityDic = {}
        for orders_Json in  self.orders_Json_list:
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

                if date not in dates:
                    dates.append(date)

                
                # GETTING THE GRATUITY MONEY
                gratuity_money = float((order["total_service_charge_money"]["amount"])/100)

                if dateGratuityDic.get(date,None) == None:
                    dateGratuityDic[date] = {
                        "gratuity":gratuity_money,
                    }
                elif dateGratuityDic.get(date,None) != None:
                    gratuity = dateGratuityDic.get(date)
                    gratuity["gratuity"] += gratuity_money
                    dateGratuityDic[date] = gratuity

        return dateGratuityDic

    