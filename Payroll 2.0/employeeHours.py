from SharedDataSingleton import SharedDataSingleton
import datetime
import json as json
from Utility import Utility
import UtilityWriteFile

class EmployeeHours:

    def __init__(self):

        self.singletonCommonData = SharedDataSingleton.getInstance()
        self.employeeDateHoursJSON = self.__getEmployeeDateHours()
        self.employeeFirstLastNameList = []
        self.employeeHoursDataByDate = self.__getEmployeeData()
        # print(self.employeeHoursDataByDate)
        self.writeToFile(self.employeeHoursDataByDate, self.employeeFirstLastNameList)
    
    
    def __getEmployeeDateHours(self):

        """
            __getEmployeeDateHours gets the employee data from the API and dumps the data into a file for inspection.
            
            :param _ :
            :return: JSON object from API
        """ 

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
                        return result.body

        elif result.is_error():
            print(result.errors)

    def __getEmployeeData(self):

        """
            __getEmployeeData extracts employee name, hours and ID from the JSON object and stores data into two sepaprate
            dictionaries. The data stored in the dictionary is in the format:
            employeeHoursDataByDate - Date: {ID, name, hours worked}
            
            :param _ :
            :return: employeeHoursDataByDate
        """

        shifts = self.employeeDateHoursJSON["shifts"]

        employeeHoursDataByID = {}
        employeeHoursDataByDate = {}

        for shift in shifts:
            
            # Getting number of hours worked in the shift.
            hours = Utility.getHours(shift["start_at"], shift["end_at"])

            # Getting the date
            date = Utility.convertUTCDateToPST(shift["start_at"])
            
            # Getting the employee information per shift.
            firstLast = self.__getTeamMember(shift["team_member_id"])
            name_pos = f"{firstLast[0]} {firstLast[1]} - {shift['wage']['title']}"

            # List of name - position for keeping track.
            if name_pos not in self.employeeFirstLastNameList:
                self.employeeFirstLastNameList.append(name_pos)

            # If the data is encountered first time in the dictionary
            if employeeHoursDataByDate.get(date, None) == None:
                employeeHoursDataByDate[date] = [

                    {
                        "ID" : shift["team_member_id"],
                        "firstName" : firstLast[0],
                        "lastName" : firstLast[1],
                        "position" : shift["wage"]["title"],
                        "hours" : hours
                    }
                ]
            
            # If the date is already present, then append the employee.
            elif employeeHoursDataByDate.get(date, None) != None:
                data = employeeHoursDataByDate[date]
                data.append(
                    {
                        "ID" : shift["team_member_id"],
                        "firstName" : firstLast[0],
                        "lastName" : firstLast[1],
                        "position" : shift["wage"]["title"],
                        "hours" : hours
                    }
                )
                employeeHoursDataByDate[date] = data

        return employeeHoursDataByDate

    def __getTeamMember(self, id):

        """
            __getTeamMember gets the team member information JSON and extracts the first and last name.
        
            :param _ :
            :return: (first name, last name)
        """
        
        result = self.singletonCommonData.client.team.retrieve_team_member(
            team_member_id = id
        )

        if result.is_success():
            team_member = result.body["team_member"]
            firstLast = (team_member["given_name"],team_member["family_name"])
        elif result.is_error():
            print(result.errors)

        return firstLast

    def writeToFile(self, employeeHoursDataByDate, employeeFirstLastNameList):

        UtilityWriteFile.UtilityWriteFile.writeEmployeeHours(employeeHoursDataByDate, employeeFirstLastNameList)