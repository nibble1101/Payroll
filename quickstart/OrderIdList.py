from square.client import Client
import os
import pprint

# print(os.environ)

# client = Client(
#     access_token=os.environ['SQUARE_ACCESS_TOKEN_SANDBOX'],
#     environment='sandbox')

def getListOfOrderId(restaurant, start_date, end_date, location):
    
    if restaurant == "Kricket":
        client = Client(
            access_token=os.environ['SQUARE_ACCESS_TOKEN_PRODUCTION_KRICKET'],
            environment='production')

        result = client.payments.list_payments(
            begin_time = start_date,
            end_time = end_date,
            location_id = location
        )
    
    elif restaurant == "Meesha":
        client = Client(
            access_token=os.environ['SQUARE_ACCESS_TOKEN_PRODUCTION_MEESHA'],
            environment='production')

        result = client.payments.list_payments(
            begin_time = start_date,
            end_time = end_date,
            location_id = location
        )

    if result.is_success():
        pprint.pprint(result.body)
    elif result.is_error():
        print(result.errors)
