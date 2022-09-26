import SharedDataSingleton as data
from OrderJsonObj import OrderJsonObj
import datetime
from pytz import timezone
import pytz

class Tips:

    def __init__(self):
        self.singletonCommonData = data.sharedDataSingleton.getInstance()
        self.dateTipsDic = {}

    def __generateDateTipDic(self):
        
        dates = []
        orders_Json = OrderJsonObj.getOrderJsonObj()
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

            
            # GETTING THE TIP MONEY
            tip_money = float((order["total_tip_money"]["amount"])/100)

            if self.dateTipsDic.get(date,None) == None:
                self.dateTipsDic[date] = {
                    "tip":tip_money,
                }
            elif self.dateTipsDic.get(date,None) != None:
                tip = self.dateTipsDic.get(date)
                tip["tip"] += tip_money
                self.dateTipsDic[date] = tip

        print(self.dateTipsDic)

    