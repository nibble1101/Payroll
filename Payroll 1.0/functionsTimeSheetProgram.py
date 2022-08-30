import csv
import datetime
from collections import OrderedDict
import copy
from re import sub

"""
2021-04-28
[{'Jack': 6.5}, {'Jon': 9.7}, {'Nahshon': 8.3}, {'Safia ': 7.18}, {'Silvia': 13.69}, {'Terry': 11.75}, {'Xavie': 8.16}, {'Yessica': 13.47}]


2021-04-29
[{'Andrea': 4.0}, {'Jon': 4.37}, {'LauraT': 6.28}, {'Nahshon': 6.34}, {'Safia ': 7.35}, {'Silvia': 13.36}, {'Terry': 11.79}, {'Xavie': 9.3}, {'Yessica': 12.04}]


2021-04-30
[{'Andrea': 4.0}, {'Jon': 6.18}, {'LauraT': 6.07}, {'Safia ': 7.49}, {'Silvia': 11.83}, {'Terry': 11.44}, {'Xavie': 8.73}, {'Yessica': 11.44}]


2021-05-01
[{'Andrea': 6.0}, {'Jon': 7.93}, {'LauraT': 6.7}, {'Safia ': 7.48}, {'Silvia': 13.52}, {'Terry': 14.26}, {'Xavie': 8.71}, {'Yessica': 13.07}]


2021-05-02
[{'LauraT': 6.37}, {'Nahshon': 8.11}, {'Safia ': 6.84}, {'Silvia': 12.92}, {'Terry': 11.36}, {'Xavie': 9.0}, {'Yessica': 4.4}]


2021-05-04
[{'Silvia': 3.29}, {'Terry': 4.2}]


2021-05-05
[{'Jack': 6.78}, {'Jon': 8.97}, {'Nahshon': 5.3}, {'Safia ': 6.06}, {'Silvia': 8.35}, {'Terry': 5.79}, {'Xavie': 6.0}, {'Yessica': 9.11}]


2021-05-06
[{'Candy': 3.87}, {'Jack': 6.29}, {'Jon': 6.58}, {'LauraT': 6.19}, {'Nahshon': 2.01}, {'Sabrina': 3.72}, {'Safia ': 6.2}, {'Silvia': 14.09}, {'Xavie': 7.31}, {'Yessica': 14.07}]


2021-05-07
[{'Andrea': 3.75}, {'Candy': 6.8}, {'Jack': 8.52}, {'Jon': 7.87}, {'LauraT': 7.9}, {'Nahshon': 7.78}, {'Safia ': 6.83}, {'Silvia': 13.7}, {'Terry': 15.18}, {'Xavie': 8.54}, {'Yessica': 13.67}]


2021-05-08
[{'Andrea': 6.23}, {'Jack': 8.02}, {'Jon': 7.54}, {'LauraT': 7.56}, {'Nahshon': 8.72}, {'Safia ': 7.59}, {'Silvia': 14.0}, {'Terry': 14.0}, {'Xavie': 8.61}]


2021-05-09
[{'Jack': 8.83}, {'Jon': 5.78}, {'LauraT': 8.86}, {'Nahshon': 6.56}, {'Sabrina': 4.95}, {'Silvia': 11.45}, {'Terry': 13.68}]

"""

def getFrontAndBackStaffTotalList(timesheetsRecord_byDate, tipPoolDictionary):

    frontHoursTotal = {}
    backHoursTotal = {}

    for date, listOfData in timesheetsRecord_byDate.items():
        frontHours = 0.0
        backHours = 0.0

        for staffRecord in listOfData:
            name = list(staffRecord.keys())[0]
            hours = list(staffRecord.values())[0]
            if tipPoolDictionary.get(name,None) == None:
                print(f"The staff name '{name}' is not found in the per hour pay master file.\nThe program exists.")
                quit()
            else:
                if tipPoolDictionary.get(name,None) == 90:
                    frontHours += hours
                elif tipPoolDictionary.get(name,None) == 10:
                    backHours += hours

        frontHoursTotal[date] = round(frontHours,4)
        backHoursTotal[date] = round(backHours,4)

    return (frontHoursTotal, backHoursTotal)

    pass

def getTipPoolDictionary(masterHourlyPay):
    tipPoolDictionary = {}
    with open(masterHourlyPay, mode='r') as file:
        reader_object = csv.reader(file, delimiter=',')
        line_count = 0
        for row in reader_object:
            if line_count == 0:
                line_count+=1
                continue

            if line_count!=0 and row != []:
                if tipPoolDictionary.get(row[0], None) != None:
                    continue
                else:
                    tipPoolDictionary[row[0]] = int(row[3])

    return tipPoolDictionary





def findFieldIndex(fields):

    """THIS FUNCTION WILL RETURN THE DICTIONARY WITH THE FIELDS AND THEIR INDEXES IN THE ROWS"""
    
    fieldIndexDicitonary = {}
    index = 0

    for field in fields:
        if field == '\ufeffStaff Name' or field == 'Staff Name':
            fieldIndexDicitonary['Staff Name'] = index
        
        elif field == '\ufeffDate' or field == 'Date':
            fieldIndexDicitonary['Date'] = index
        
        elif field == '\ufeffPayable(Reg. Hrs)' or field == 'Payable(Reg. Hrs)':
            fieldIndexDicitonary['Payable(Reg. Hrs)'] = index
        
        elif field == '\ufeffStaff Type' or field == 'Staff Type':
            fieldIndexDicitonary['Staff Type'] = index
        
        elif field == '\ufeffReg. Rate of Pay' or field == 'Reg. Rate of Pay':
            fieldIndexDicitonary['Reg. Rate of Pay'] = index

        index+=1

    return fieldIndexDicitonary



def horizontalSums(rows):

    '''THIS FUNCTION WILL CALCULATE THE SUM OF EACH ROW AND WILL RETURN A LIST'''

    sumList = []
    for row in rows:
        sum = 0
        for ele in row:
            if type(ele) == float:
                sum+=ele
        sumList.append(round(sum,4))
    
    return sumList

def verticalSums(rows, numberOfNames):

    '''THIS FUNCTION WILL CALCULATE EACH COLUMN SUM AND WILL RETURN A LIST'''

    index = 1
    sumList = []
    for i in range(0,numberOfNames):
        sum = 0
        for row in rows:
            if type(row[index]) == float:
                sum+=row[index]
        index+=1
        sumList.append(round(sum,4))
        
    return sumList


def makeDictionaries(timeSheet):

    '''THIS FUNCTION WILL MAKE THE TWO REQUIRED DICTIONARIES BY NAME AND BY DATE AND THEN RETURN THEM'''

    timesheetsRecord_byDate = {} # DICTIONARIES FOR THE RECORDS ARRANGED BY DATE

    timesheetsRecord_byName = {} # DICTIONARIES FOR THE RECORDS ARRANGED BY NAMES


    with open(timeSheet, mode = 'r') as timesheets: #OPENING FILE FOR READING

        reader_object = csv.reader(timesheets, delimiter=',') 
        line_count = 0 #LINE COUNT TO FOR PARSING

        for row in reader_object:

            if(line_count == 0): #IGNORES THE FIELDS FROM THE READER FILE
                fieldIndexDicitonary = findFieldIndex(row) #GETTING THE INDEXES OF THE FIELD NAMES FROM THE FILE.
                line_count+=1
                pass

            else:
                #EXTRACTING RELEVANT DATA FROM THE ROW
                if(row[fieldIndexDicitonary.get('Date')] != ''): #CHECK TO AVOID EMPTY LINE PROCESSING
                    staffName = row[fieldIndexDicitonary.get('Staff Name')]
                    date = datetime.datetime.strptime(row[fieldIndexDicitonary.get('Date')], '%d-%b-%y').date()
                    date_hr_dict = {}
                    date_hr_dict[date] = []
                    payable_hr = float(row[fieldIndexDicitonary.get('Payable(Reg. Hrs)')])

                    # if(payable_hr > 14): #PRINTS ALL THE ENTERIES WITH THE PAYABLE HOURS GREATER THAN 14 HRS
                    #     print(row)

                    if(payable_hr != 0):
                        if timesheetsRecord_byName.get(staffName, 0) == 0:
                            timesheetsRecord_byName[staffName] = [date_hr_dict]

                        else:
                            timesheetsRecord_byName[staffName].append(date_hr_dict)

                    if payable_hr != 0:
                        li = timesheetsRecord_byName[staffName]

                        for dates in li:

                            if dates.get(date, None) != None:
                                dates.get(date).append(payable_hr)

                if(row[fieldIndexDicitonary.get('Date')] != ''):  #CHECK TO AVOID EMPTY LINE PROCESSING
                    staffName = row[fieldIndexDicitonary.get('Staff Name')]
                    date = datetime.datetime.strptime(row[fieldIndexDicitonary.get('Date')], '%d-%b-%y').date()
                    staff_hr_dict = {}
                    staff_hr_dict[staffName] = 0 #
                    payable_hr = float(row[fieldIndexDicitonary.get('Payable(Reg. Hrs)')])
            
                    if payable_hr != 0:
                        if timesheetsRecord_byDate.get(date, None) == None: #
                            timesheetsRecord_byDate[date] = [staff_hr_dict] #

                        elif timesheetsRecord_byDate.get(date, None) != None:
                            li = timesheetsRecord_byDate[date]
                            flag = 0

                            for staffRecords in li: ##
                                if staffRecords.get(staffName, None) != None:
                                    flag = 1
                                    break

                            if flag == 0:
                                    timesheetsRecord_byDate[date].append(staff_hr_dict) #

                    if payable_hr != 0:
                        li = timesheetsRecord_byDate[date] #

                        for staffRecords in li: ##

                            if staffRecords.get(staffName, None) != None: ##
                                hours = staffRecords.get(staffName) + payable_hr ##
                                staffRecords[staffName] = round(hours,4)

    timesheetsRecord_byName = OrderedDict(sorted(timesheetsRecord_byName.items()))

    timesheetsRecord_byDate = dict(OrderedDict(sorted(timesheetsRecord_byDate.items())))

    # for k,v in timesheetsRecord_byDate.items():
    #     print(k)
    #     print(v)
    #     print("\n")

    return (timesheetsRecord_byDate, timesheetsRecord_byName)

def calculateSum(rows, numberOfNames):

    '''CALCULATES THE SUM OF THE ROWS AND COLUMNS AND RETURNS THE DATA'''

    sumListPerDay = horizontalSums(rows)
    grandTotalPerDaySum = sum(sumListPerDay)
    sumListPerName = verticalSums(rows, numberOfNames)
    grandTotalPerNameSum = sum(sumListPerName)

    return (sumListPerDay,round(grandTotalPerDaySum,4),sumListPerName,round(grandTotalPerNameSum,4))


def writeToTheFile(finalHourPerDateTable, finalPayRows):

    '''WRITING THE TABLE TO THE FILE IN CSV FORM'''

    row = [] #FOR WRITING EMPTY ROWS TO THE FILE
    


    with open('timesheetCalculations.csv', mode='w') as calculations: #WRITING DATA TO THE FILE
        calculation_obj = csv.writer(calculations, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        calculation_obj.writerows(finalHourPerDateTable)
        calculation_obj.writerow(row)
        calculation_obj.writerow(row)
        calculation_obj.writerow(row)
        calculation_obj.writerow(row)
        calculation_obj.writerows(finalPayRows)



def createHourlyPayInfo(masterHourlyPay):

    '''THIS FUNCTION WILL READ THE HOURLY PAY CSV FILE AND WILL STORE THE DATA IN A DICTIONARY.'''


    hourlyPayInfo = {} #DICTIONARY TO STORE THE HOURLY PAY INFORMATION
    with open(masterHourlyPay, mode = 'r') as paysheet: #OPENING FILE FOR READING

        reader_object = csv.reader(paysheet, delimiter=',') 
        line_count = 0 #LINE COUNT TO FOR PARSING

        for row in reader_object:

            if(line_count == 0): #IGNORES THE FIELDS FROM THE READER FILE
                fieldIndexDicitonary = findFieldIndex(row)
                line_count+=1
                pass
            
            else:
                if row == []:
                    break
                staffName = row[fieldIndexDicitonary.get('Staff Name')] # FOR STORING THE STAFF NAME
                staffType = row[fieldIndexDicitonary.get('Staff Type')] # FOR STORING THE STAFF TYPE
                rateOfPay = row[fieldIndexDicitonary.get('Reg. Rate of Pay')] # FOR STORING THE RATE OF PAY
                rateOfPay = float(sub(r'[^\d.]', '', rateOfPay))
                rateOfPay = round(rateOfPay,4)
                typePay = (staffType, rateOfPay)
                hourlyPayInfo[staffName] = typePay
                
    return hourlyPayInfo

def createTableGrossPay(hourlyPayInfo, rows, fields, grandTotalRow, finalPayInfoRow, finalPayRows, grandTotalPerDaySum):

    '''THIS FUNCTION RETURNS THE FINAL TABLE OF THE GROSS INCOME'''
    
    index = 0
    grandTotalPerNameSumPos = len(rows)-1
    grandTotalOfGrossPay = 0
    for name in fields:
        if index == 0:
            index+=1
            continue
        else:
            if(name == 'GRAND TOTAL'):
                continue
            if hourlyPayInfo.get(name , None) == None:
                print(f"Hourly Pay rate for '{name}' is not found in the master file. \nThe program quits.\nPlease fix the master file before re running")
                quit()
            hourlyPayRate = hourlyPayInfo.get(name)[1]
            #print(grandTotalRow[index])
            sumOfGrossPay = round(hourlyPayRate*grandTotalRow[index],4)
            finalPayInfoRow.append(name)
            finalPayInfoRow.append(grandTotalRow[index])
            finalPayInfoRow.append(sumOfGrossPay)
            grandTotalOfGrossPay+=sumOfGrossPay

        finalPayRows.append(finalPayInfoRow)
        index+=1
        finalPayInfoRow = []

    finalPayRows.append(['GRAND TOTAL',grandTotalPerDaySum,grandTotalOfGrossPay])
    return finalPayRows