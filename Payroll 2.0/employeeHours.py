from SharedDataSingleton import SharedDataSingleton
import datetime
import json as json

class EmployeeHours:

    def __init__(self):

        self.singletonCommonData = SharedDataSingleton.getInstance()
        self.EmployeeDateHours = self.__getEmployeeDateHours()

    
    
    def __getEmployeeDateHours(self):

        startDate = datetime.datetime.strptime(self.singletonCommonData.pacificStartDate, "%m-%d-%Y")
        endDate = datetime.datetime.strptime(self.singletonCommonData.pacificEndDate, "%m-%d-%Y")
        startDate = str(startDate).split()[0]
        endDate = str(endDate).split()[0]

        result = self.singletonCommonData.client.labor.search_shifts(
            body = {
                "query": {
                    "filter": {
                        "workday": {
                            "date_range": {
                                "start_date": startDate,
                                "end_date": endDate
                            },
                        }
                    }
                },
                "limit": 200
            }
        )

        if result.is_success():
            with open("employeeHours.json", "w") as outfile:
                        json.dump(result.body, outfile, indent = 4)
        elif result.is_error():
            print(result.errors)