from typing import List
from OrderJsonObj import OrderJsonObj
import datetime
from pytz import timezone
import pytz
from Utility import Utility

class Tips:

    def __init__(self,  orders_Json_list):
        self.orders_Json_list =  orders_Json_list
        self.dateTipsDic = self.__generateDateTipDic()

    def __generateDateTipDic(self):
        
        dates = []
        dateTipsDic = {}
        for orders_Json in  self.orders_Json_list:
            
            for order in orders_Json["orders"]:

                # GETTING THE DATE OF THE ORDER.
                date = order["created_at"]

                # FIXING THE DATE FROM UTC TO PST
                date = Utility.convertUTCDateToPST(date)

                if date not in dates:
                    dates.append(date)

                
                # GETTING THE TIP MONEY
                tip_money = float((order["total_tip_money"]["amount"])/100)

                if dateTipsDic.get(date,None) == None:
                    dateTipsDic[date] = {
                        "tip":tip_money,
                    }
                elif dateTipsDic.get(date,None) != None:
                    tip = dateTipsDic.get(date)
                    tip["tip"] += tip_money
                    dateTipsDic[date] = tip

        return dateTipsDic

    