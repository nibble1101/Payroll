import json

class JsonParser:

    @staticmethod
    def extractOrderIDList(json_dict_payment_object):

        # ORDER IDs LIST OF THE DAY
        order_ID_list = []

        # GETTING THE PAYMENT LIST FROM THE JSON OBJECT OF THE DAY.
        list_of_payments = json_dict_payment_object["payments"]

        # TRAVERSING THE PAYMENTS FROM THE DAY AND GETTING THE ORDER ID OF EACH PAYMENT.
        for payment in list_of_payments:
            order_ID_list.append(payment["order_id"])

        # with open("PaymentAPI.json", "w") as outfile:
        #     json.dump(json_dict_payment_object, outfile, indent = 4)

        return order_ID_list

