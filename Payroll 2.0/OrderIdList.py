import SharedDataSingleton as data
import JsonParser as jp

class OrderID:

    @staticmethod
    def getListOfOrderId():
        """
            Description: This function takes the restaurant name Form payment API.
        """

        singletonCommonData = data.sharedDataSingleton.getInstance()
        listOfOrders = None

        result = singletonCommonData.client.payments.list_payments(
            begin_time = singletonCommonData.startDate,
            end_time = singletonCommonData.endDate,
            location_id = singletonCommonData.restaurant.location_id
        )

        if result.is_success():
            json_dict_object = result.body
            listOfOrders = jp.extractOrderList(json_dict_object)
            return listOfOrders
        elif result.is_error():
            print(result.errors)