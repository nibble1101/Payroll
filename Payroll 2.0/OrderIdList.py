from SharedDataSingleton import SharedDataSingleton
from JsonExtractor import JsonParser
import datetime

class OrderID:

    @staticmethod
    def getListOfOrderId():
        """
        Description:    Gets the list of Order ID from the Payments API and 

        Parameters:

        Returns:        Return the Lists of List Order ID each day.

        """

        # INSTANTIATE SINGLETON CLASS
        singletonCommonData = SharedDataSingleton.getInstance()

        # LIST OF ORDER IDs
        listOfOrders = []

        # INITIAL BEGIN TIME WILL BE THE BEGIN DATE ENTERED BY THE USER.
        begin = datetime.datetime.strptime(singletonCommonData.startDate, "%Y-%m-%dT%H:%M:%S%z")

        # INITIAL END DATE WILL BE +24 HOURS
        end = begin + datetime.timedelta(hours=23, minutes=59)

        # LOOPING OVER ALL THE DAYS TO GET THE LIST OF THE ORDER IDs
        for i in range(0, singletonCommonData.numberOfDays+1):
            
            # API CALL WILL RETURN JSON OBJECT WITH THE PAYMENT OF THE ORDERS
            result = singletonCommonData.client.payments.list_payments(
                begin_time = begin.isoformat(),
                end_time = end.isoformat(),
                location_id = singletonCommonData.restaurant.location_id
            )

            if result.is_success():
                if result.body != {}:
                    json_dict_object = result.body

                    # EXTRACT THE LIST OF THE ORDER IDs FROM THE JSON OJECT USING THE UTILITY FUNCTION.
                    listOfOrders.append(JsonParser.extractOrderList(json_dict_object))

            elif result.is_error():
                print(result.errors)

            # UPDATING THE DATE BY ADDING +24 HOURS TO BOTH START AND END DATE.
            begin = begin + datetime.timedelta(hours=24)
            end = end + datetime.timedelta(hours=24)

        return listOfOrders