from functionsTimeSheetProgram import *
from functionsTransactionsProgram import *
import sys
import functionsPaymentDetails  as paymentDetails


# MAIN FUNCTION

if __name__ == "__main__":

    #GETTING THE COMMAND LINE ARGUMENTS
    listOfArguments = sys.argv
    if len(listOfArguments) < 8:
        print('Inadequate number of arguments. Program exits safely.')
        quit()
    timeSheet = listOfArguments[1]
    transactionSheet = listOfArguments[2]
    paymentDetailsSheet = listOfArguments[3]
    masterHourlyPay = listOfArguments[4]
    masterExperience = listOfArguments[5]
    masterTockExperiences = listOfArguments[6]
    startDate = listOfArguments[7]

    # timeSheet = 'timesheets.csv'
    # transactionSheet = 'transactions.csv'
    # paymentDetailsSheet = 'paymentDetails.csv'
    # masterHourlyPay = 'MASTERhourlyPay.csv'
    # masterExperience = 'MASTERexperience.csv'
    #masterTockExperiences = 'MASTERtockExperiences.csv'

    startDate = datetime.datetime.strptime(startDate, '%m/%d/%y').date()


    #FUNCTION CALL FOR RECORDS BY DATE AND NAME
    timesheetsRecord_byDate, timesheetsRecord_byName = makeDictionaries(timeSheet)

    tipPoolDictionary = getTipPoolDictionary(masterHourlyPay)


    nameList = list(timesheetsRecord_byName.keys()) #LIST OF ALL THE EMPLOYEE NAMES

    fields = list(timesheetsRecord_byName.keys()) #INCOMPLETE ROW FOR THE FIELDS
    fields.insert(0,'Dates/Names')
    fields.append('GRAND TOTAL')

    rows = [] #CREATING THE TABLE VARIABLE

    dates = timesheetsRecord_byDate.keys() #LIST OF THE DATES

    #CREATING THE RAW TABLE 
    for date in dates:

        row = []
        for i in range(len(fields)-1):
            row.append(' ')
        li = timesheetsRecord_byDate.get(date)
        for dicts in li:

            name = list(dicts.keys())[0]
            payable_hr = list(dicts.values())[0]
            index = fields.index(name)
            row[index] = payable_hr
            
        row[0] = date
        
        rows.append(row)

    #CALCULATING THE SUM OF THE ROWS AND THE COLUMNS
    sumListPerDay, grandTotalPerDaySum, sumListPerName, grandTotalPerNameSum = calculateSum(rows, len(nameList))
    # print(grandTotalPerNameSum)
    # print(grandTotalPerDaySum)
    if grandTotalPerNameSum != grandTotalPerDaySum:
        print('***** CALCULATION ERROR *****\n\n***** PROGRAM EXISTS SAFELY *****')
        quit()


    #ADDING THE SUMS AT THE END OF EACH ROWS
    index = 0
    for row in rows:
        row.append(sumListPerDay[index])
        index+=1
    
    #CREATING THE LAST GRANDTOTAL ROW PER NAME
    grandTotalRow = copy.deepcopy(sumListPerName)
    grandTotalRow.insert(0,'GRAND TOTAL')
    grandTotalRow.append(grandTotalPerDaySum)

    # for row in rows:
    #     print(row)


    finalPayRows = [] # THIS WILL STORE THE CALCULATED WAGE OF EACH EMPLOYEE
    finalPayInfoRow = [] # THIS WILL STORE THE PAY INFO FOR EACH NAME
    hourlyPayInfo = {} # DICTIONARY STORES THE HOURLY PAY INFORMATION

    li = []
    li.append('Staff Names')
    li.append('Sum of Shift Length (hrs)')
    li.append('Sum of Gross Pay')
    finalPayRows.append(li)

    hourlyPayInfo = createHourlyPayInfo(masterHourlyPay) # CREATING THE DICTIONARY FOR HOURLY PAY

    finalPayRows = createTableGrossPay(hourlyPayInfo, rows, fields, grandTotalRow, finalPayInfoRow, finalPayRows, grandTotalPerDaySum) # CREATING THE GROSS PAY TABLE

    # WRITING DATA TO THE FILE
    finalHourPerDateTable = []
    finalHourPerDateTable.append(fields)
    for row in rows:
        finalHourPerDateTable.append(row)
    finalHourPerDateTable.append(grandTotalRow)
    writeToTheFile(finalHourPerDateTable, finalPayRows)

    frontHoursTotal, backHoursTotal = getFrontAndBackStaffTotalList(timesheetsRecord_byDate, tipPoolDictionary)


########################################################################################################################

    # TRANSACTTION CALCULATIONS

########################################################################################################################

    transactionsRecord_byDate, experienceList, dateList = dataExtraction(transactionSheet, startDate)
    relevantExperiences = relevantExperiencesList(masterExperience)
    tockExperiences = paymentDetails.extractTockExperiences(masterTockExperiences)
    listOfgratuityTockList = createOutputFile(transactionsRecord_byDate, experienceList, dateList, relevantExperiences, tockExperiences)

    # for k,v in transactionsRecord_byDate.items():
    #     print(k)
    #     print(v)


############################################################################################################################

#PAYMENT DETAILS

############################################################################################################################


finalTableOfSum = paymentDetails.extractData(paymentDetailsSheet, listOfgratuityTockList, tockExperiences)
totalGratuityColumn = paymentDetails.extractTotalGratuityColumn(finalTableOfSum)
finalOutputTable = paymentDetails.createFinalOutputTable(finalHourPerDateTable,totalGratuityColumn, frontHoursTotal, backHoursTotal, timesheetsRecord_byDate, tipPoolDictionary)


paymentDetails.outputFile(finalTableOfSum, finalOutputTable)








