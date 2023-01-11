from square.client import Client

import JsonExtractor as jp

from Tips import Tips
from Gratuity import Gratuity

from OrderJsonObj import OrderJsonObj
from UtilityWriteFile import UtilityWriteFile
from OrderIdList import OrderID

from employeeHours import EmployeeHours

class Payroll:

    def __init__(self):
        self.tip_dic = {}
        self.gratuity_dic = {}
    
    def generateTip(self, orders_Json_list):

        self.tip_dic = Tips(orders_Json_list).dateTipsDic
        print(self.tip_dic)

    def generateGratuity(self, orders_Json_list):
        
        self.gratuity_dic = Gratuity(orders_Json_list).dateGratuityDic
        print(self.gratuity_dic)

    def generatePayroll(self):
        """

        Description: Calls the necessary functions to run the payroll.
        
        """
        # GETTING THE LIST OF THE ORDER IDs IN A DAY.
        list_of_order_id_list = OrderID.getListOfOrderId()
        # GETS THE ORDER LIST AS A LIST OF JSON OBJECT OF EACH DATE.
        orders_Json_list = OrderJsonObj.getOrderJsonObj(list_of_order_id_list)
        

        # EXTRACTING TIPS AND GRATUITY
        # self.generateTip(orders_Json_list)
        # self.generateGratuity(orders_Json_list)

        # self.tip_dic, self.gratuity_dic = UtilityWriteFile.writeTipsGratuity(self.tip_dic, self.gratuity_dic)

        obj = EmployeeHours()