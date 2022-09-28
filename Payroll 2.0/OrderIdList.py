from SharedDataSingleton import SharedDataSingleton
from JsonExtractor import JsonParser
import datetime

class OrderID:

    @staticmethod
    def getListOfOrderId():
        """
        Description:    Gets the list of Order ID from the Payments API and 

        Parameters:

        Returns:        Return the Lists of List Order ID per day.

        """

        singletonCommonData = SharedDataSingleton.getInstance()
        listOfOrders = []

        
        begin = datetime.datetime.strptime(singletonCommonData.startDate, "%Y-%m-%dT%H:%M:%S%z")
        end = begin + datetime.timedelta(hours=23, minutes=59)

        for i in range(0, singletonCommonData.numberOfDays+1):


            result = singletonCommonData.client.payments.list_payments(
                begin_time = begin.isoformat(),
                end_time = end.isoformat(),
                location_id = singletonCommonData.restaurant.location_id
            )

            if result.is_success():
                if result.body != {}:
                    json_dict_object = result.body
                    listOfOrders.append(JsonParser.extractOrderList(json_dict_object))
            elif result.is_error():
                print(result.errors)

            begin = begin + datetime.timedelta(hours=24)
            end = end + datetime.timedelta(hours=24)

        for orders in listOfOrders:
            print(len(orders))
        return listOfOrders