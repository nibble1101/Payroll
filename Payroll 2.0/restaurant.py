import os

class Restaurant:

    def __init__(self, name, location_id):

        self.name = name
        self.location_id = location_id
        self.production_access_token = f'SQUARE_ACCESS_TOKEN_PRODUCTION_{(self.name).upper()}'