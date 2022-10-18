from SharedDataSingleton import SharedDataSingleton
from OrderIdList import OrderID
import json as json

class OrderJsonObj:

    @staticmethod
    def getOrderJsonObj():

        # LIST OF THE ORDER JSON OBJECTS.
        orders_Json_list = []

        singletonCommonData = SharedDataSingleton.getInstance()

        # GETTING THE LIST OF THE ORDER IDs IN A DAY.
        list_of_order_id_list = OrderID.getListOfOrderId()
        
        # TRAVERSING EACH ORDER ID LIST OF EACH DAY.
        for order_id_list in list_of_order_id_list:

            result = singletonCommonData.client.orders.batch_retrieve_orders(
            body = {
                "location_id": singletonCommonData.restaurant.location_id,
                "order_ids": order_id_list
            }
            )

            if result.is_success():
                if result.body != {}:
                    with open("orderAPI.json", "w") as outfile:
                        json.dump(result.body, outfile, indent = 4)
                    
                    # APPENDING THE ORDER JSON OBJECT WITH TIP AND GRATUITY INFO.
                    orders_Json_list.append(result.body)

            elif result.is_error():
                print(result.errors)

        return orders_Json_list