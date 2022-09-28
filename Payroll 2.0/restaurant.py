from square.client import Client
import os

class Restaurant:

    def __init__(self, name):

        self.name = name
        self.production_access_token = f'SQUARE_ACCESS_TOKEN_PRODUCTION_{(self.name).upper()}'
        self.location_id = self.__getLocationId()

    def __getLocationId(self):

        client = Client(
        access_token=os.environ[f'{self.production_access_token}'],
        environment='production')

        result = client.locations.list_locations()

        if result.is_success():
            if result.body != {}:
                for location in result.body['locations']:
                    return location['id']

        elif result.is_error():
            for error in result.errors:
                print(error['category'])
                print(error['code'])
                print(error['detail'])
