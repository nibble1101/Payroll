from square.client import Client
import os
import JsonExtractor as jp
import json
from Tips import Tips
from Gratuity import Gratuity
import datetime
from pytz import timezone
import pytz
from OrderJsonObj import OrderJsonObj
from UtilityWriteFile import UtilityWriteFile

class Payroll:

    def __init__(self):
        self.tip_dic = {}
        self.gratuity_dic = {}
    
    def generateTipFile(self, orders_Json_list):

        self.tip_dic = Tips(orders_Json_list).dateTipsDic
        print(self.tip_dic)

    def generateGratuityFile(self, orders_Json_list):
        
        self.gratuity_dic = Gratuity(orders_Json_list).dateGratuityDic
        print(self.gratuity_dic)

    def generatePayroll(self):
        """

        Description: Calls the necessary functions to run the payroll.
        
        """
        
        # GETS THE ORDER LIST AS A LIST OF JSON OBJECT OF EACH DATE.
        orders_Json_list = OrderJsonObj.getOrderJsonObj()

        # EXTRACTING TIPS AND GRATUITY
        self.generateTipFile(orders_Json_list)
        self.generateGratuityFile(orders_Json_list)

        UtilityWriteFile.writeTipsGratuity(self.tip_dic, self.gratuity_dic)