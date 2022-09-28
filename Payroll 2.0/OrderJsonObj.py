from SharedDataSingleton import SharedDataSingleton
import OrderIdList
import json as json

class OrderJsonObj:

    @staticmethod
    def getOrderJsonObj():

        singletonCommonData = SharedDataSingleton.getInstance()
        result = singletonCommonData.client.orders.batch_retrieve_orders(
        body = {
            "location_id": singletonCommonData.restaurant.location_id,
            "order_ids": OrderIdList.OrderID.getListOfOrderId()
          }
        )

        if result.is_success():
            with open("orderAPI.json", "w") as outfile:
                json.dump(result.body, outfile, indent = 4)
            return result.body

        elif result.is_error():
            print(result.errors)