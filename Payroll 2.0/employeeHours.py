from SharedDataSingleton import SharedDataSingleton
import datetime
import json as json
from Utility import Utility

class EmployeeHours:

    def __init__(self):

        self.singletonCommonData = SharedDataSingleton.getInstance()
        self.EmployeeDateHours = self.__getEmployeeDateHours()
        self.employeeData = self.__getEmployeeData()
        # self.teamMemberIDNameDic = self.__getTeamMember()
        # print(self.teamMemberIDNameDic)
    
    
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
                        return result.body

        elif result.is_error():
            print(result.errors)

    def __getEmployeeData(self):

        shifts = self.EmployeeDateHours["shifts"]

        employeeHoursDataByID = {}
        employeeHoursDataByDate = {}

        for shift in shifts:
            
            # Getting number of hours worked in the shift.
            hours = Utility.getHours(shift["start_at"], shift["end_at"])

            # Getting the date
            date = Utility.convertUTCDateToPST(shift["start_at"])
            

            # Employee Data by ID
            if employeeHoursDataByID.get(shift["team_member_id"], None) == None:
                firstLast = self.__getTeamMember(shift["team_member_id"])
                employeeHoursDataByID[shift["team_member_id"]] = {
                    "firstName" : firstLast[0],
                    "lastName" : firstLast[1],
                    "position" : shift["wage"]["title"],
                    "hours" : hours
                }

            elif employeeHoursDataByID.get(shift["team_member_id"], None) != None:
                data = employeeHoursDataByID[shift["team_member_id"]]
                data["hours"] = round((data["hours"] + hours), 2)
                employeeHoursDataByID[shift["team_member_id"]] = data

            # Employee Data by Date

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

        print(employeeHoursDataByDate.keys())

        return employeeHoursDataByID, employeeHoursDataByDate

    def __getTeamMember(self, id):

        
        result = self.singletonCommonData.client.team.retrieve_team_member(
            team_member_id = id
        )

        if result.is_success():
            team_member = result.body["team_member"]
            firstLast = (team_member["given_name"],team_member["family_name"])
        elif result.is_error():
            print(result.errors)

        return firstLast

