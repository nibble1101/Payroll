from SharedDataSingleton import SharedDataSingleton
from JsonExtractor import JsonParser
import datetime

class OrderID:

    @staticmethod
    def getListOfOrderId():
        """
            Description: This function takes the restaurant name Form payment API.
        """

        singletonCommonData = SharedDataSingleton.getInstance()
        listOfOrders = []

        
        begin = datetime.datetime.strptime(singletonCommonData.startDate, "%Y-%m-%dT%H:%M:%S%z")
        end = begin + datetime.timedelta(hours=23, minutes=59)

        result = singletonCommonData.client.payments.list_payments(
            begin_time = begin.isoformat(),
            end_time = end.isoformat(),
            location_id = singletonCommonData.restaurant.location_id
        )

        if result.is_success():
            json_dict_object = result.body
            listOfOrders.append(JsonParser.extractOrderList(json_dict_object))
        elif result.is_error():
            print(result.errors)

        for i in range(0,singletonCommonData.numberOfDays):

            begin = begin + datetime.timedelta(hours=24)
            end = end + datetime.timedelta(hours=24)
            print(begin)
            print(end)
            result = singletonCommonData.client.payments.list_payments(
                begin_time = begin.isoformat(),
                end_time = end.isoformat(),
                location_id = singletonCommonData.restaurant.location_id
            )

            if result.is_success():
                if result.body != None:
                    json_dict_object = result.body
                    listOfOrders.append(JsonParser.extractOrderList(json_dict_object))
                # print(len(listOfOrders))
                # return listOfOrders
            elif result.is_error():
                print(result.errors)

        # for orders in listOfOrders:
        #     # print(len(orders))
        return listOfOrders