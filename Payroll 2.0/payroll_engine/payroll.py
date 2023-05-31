from Tips import Tips
from Gratuity import Gratuity

from OrderJsonObj import OrderJsonObj
from UtilityWriteFile import UtilityWriteFile
from OrderIdList import OrderID

from employeeHours import EmployeeHours


# Plan of action for getting tips and gratuity:
# 1. First get the list of all the order IDs per day
# 2. Get the JSON list of all the orders from the orderID list
# 3. Parse the JSON list and calculate the tip and Gratuity


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
        listOfListOfOrderIDs_perDay = OrderID.getListOfOrderId()
        # GETS THE ORDER LIST AS A LIST OF JSON OBJECT OF EACH DATE.
        orders_Json_list = OrderJsonObj.getOrderJsonObj(listOfListOfOrderIDs_perDay)
        

        # EXTRACTING TIPS AND GRATUITY
        # self.generateTip(orders_Json_list)
        # self.generateGratuity(orders_Json_list)

        # self.tip_dic, self.gratuity_dic = UtilityWriteFile.writeTipsGratuity(self.tip_dic, self.gratuity_dic)

        obj = EmployeeHours()