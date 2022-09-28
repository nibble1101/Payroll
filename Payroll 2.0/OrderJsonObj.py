from SharedDataSingleton import SharedDataSingleton
import OrderIdList
import json as json

class OrderJsonObj:

    @staticmethod
    def getOrderJsonObj():

        orders_Json_list = []
        singletonCommonData = SharedDataSingleton.getInstance()
        list_of_order_id_list = OrderIdList.OrderID.getListOfOrderId()
        
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
                    orders_Json_list.append(result.body)

            elif result.is_error():
                print(result.errors)

        return orders_Json_list