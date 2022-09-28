import json

class JsonParser:

    @staticmethod
    def extractOrderList(json_dict_payment_object):

        order_list = []

        list_of_payments = json_dict_payment_object["payments"]

        for payment in list_of_payments:
            order_list.append(payment["order_id"])

        with open("PaymentAPI.json", "w") as outfile:
            json.dump(json_dict_payment_object, outfile, indent = 4)

        return order_list

