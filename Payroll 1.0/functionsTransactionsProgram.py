import csv
import datetime
from collections import OrderedDict
import copy
from re import sub

"""

transactionsRecord_byDate = {

    'Transaction Date' : [
        {'To Go DoorDash' : [{'pay' : []},{'pay' : []},{'pay' : []}]},
        {'To Go Pick Up' : [{'pay' : []},{'pay' : []},{{'pay' : []}]},
        {'Patio' : [{{'pay' : []},{{'pay' : []},{{'pay' : []}]},
    ]
}

"""


def findFieldIndex(fields):

    """THIS FUNCTION WILL RETURN THE DICTIONARY WITH THE FIELDS AND THEIR INDEXES IN THE ROWS"""
    
    fieldIndexDictionary = {}
    index = 0

    for field in fields:
        if field == '\ufeffRealized Date' or field == 'Realized Date':
            fieldIndexDictionary['Realized Date'] = index
        
        elif field == '\ufeffExperience' or field == 'Experience':
            fieldIndexDictionary['Experience'] = index
        
        elif field == '\ufeffService Charge Rate' or field == 'Service Charge Rate':
            fieldIndexDictionary['Service Charge Rate'] = index

        elif field == '\ufeffGratuity Charge' or field == 'Gratuity Charge':
            fieldIndexDictionary['Gratuity Charge'] = index

        elif field == '\ufeffPayment Refunded' or field == 'Payment Refunded':
            fieldIndexDictionary['Payment Refunded'] = index

        elif field == '\ufeffNet Payout Amount' or field == 'Net Payout Amount':
            fieldIndexDictionary['Net Payout Amount'] = index

        elif field == '\ufeffAction' or field == 'Action':
            fieldIndexDictionary['Action'] = index

        index+=1

    return fieldIndexDictionary

def relevantExperiencesList(masterExperience):
    with open(masterExperience, mode = 'r') as master: #OPENING FILE FOR READING

        relevantExperience = []
        reader_object = csv.reader(master, delimiter=',') 
        line_count = 0 #LINE COUNT TO FOR PARSING

        for row in reader_object: # PROCESSING ONE ROW AT A TIME
            if line_count == 0 or row == []:
                line_count+=1
                continue
            else:
                relevantExperience.append(row[0])

    return relevantExperience

def dataExtraction(transactionSheet, startDate):

    '''THIS FUNCTION WILL EXTRACT RELEVANT INFORMATION AND THEN IT RETURNS THE DICTIONARY OF THE DATA'''

    endDate = startDate + datetime.timedelta(days=13)
    print(f"The end date is: '{endDate}")
    transactionsRecord_byDate = {} # DICTIONARIES FOR THE RECORDS ARRANGED BY DATE

    dateList = [] # LISTS OF THE DATES ENCOUNTERED
    fields = [] # LIST OF THE FIELDS READ IN FROM THE FILE
    fieldIndexDictionary = {} # DICTIONARY WHICH STORES THE INDEX OF THE FIELDS

    expericenceList = []

    with open(transactionSheet, mode = 'r') as timesheets: #OPENING FILE FOR READING

        reader_object = csv.reader(timesheets, delimiter=',') 
        line_count = 0 #LINE COUNT TO FOR PARSING

        for row in reader_object: # PROCESSING ONE ROW AT A TIME

            if(line_count == 0): #IGNORES THE FIELDS FROM THE READER FILE
                fields = copy.deepcopy(row)
                fieldIndexDictionary = findFieldIndex(fields) #FUNCTION CALL FOR CREATION OF THE DICTIONARY WHICH STORES THE INDEX OF THE FILEDS
                #print(fieldIndexDictionary)
                line_count+=1

            else:
                date = row[fieldIndexDictionary.get('Realized Date')]

                if date == '':
                    break
                if date != '':  #CHECK TO AVOID EMPTY LINE PROCESSING
                    
                    #EXTRACTING DATA FROM THE ROW
                    experience = row[fieldIndexDictionary.get('Experience')] 
                    if not experience in expericenceList: # CREATING THE LIST OF THE EXPERIENCES
                        expericenceList.append(experience)
                    if row[fieldIndexDictionary.get('Gratuity Charge')] == '':
                        gratuity = 0.0
                    else:
                        gratuity = round(float(row[fieldIndexDictionary.get('Gratuity Charge')]),4)
                    if row[fieldIndexDictionary.get('Service Charge Rate')] == '':
                        service = 0.0
                    else:
                        service = round(float(row[fieldIndexDictionary.get('Service Charge Rate')]),4)
                    if row[fieldIndexDictionary.get('Payment Refunded')] == '':
                        refund = 0.0
                    else:
                        refund =  round(float(row[fieldIndexDictionary.get('Payment Refunded')]),4)
                    if row[fieldIndexDictionary.get('Net Payout Amount')] == '':
                        payable = 0.0
                    else:
                        payable = round(float(row[fieldIndexDictionary.get('Net Payout Amount')]),4)
                    date = datetime.datetime.strptime(date, '%m/%d/%y').date()

                    if date>endDate or date<startDate:
                        continue

                    if date not in dateList:
                        dateList.append(date)
                    if row[fieldIndexDictionary.get('Action')] == '':
                        action = None
                    else:
                        action = row[fieldIndexDictionary.get('Action')]

                    #if action == 'BOOKED' or action == 'REFUNDED': # ONLY PROCESS THE DATA WHICH HAS THE ACTION BOOKED
                    if action == 'BOOKED':

                        experienceDictionary = {} #DICTIONARY OF PER EXPERIENCE
                        experienceDictionary[experience] = [] #APPENDING AN EMPTY LIST
                        

                        # EMPTY DICTIONARIES PER EXPERIENCES
                        gratuityLi = {}
                        serviceLi = {}
                        refundLi = {}
                        payableLi = {}

                        if transactionsRecord_byDate.get(date, None) == None: #WHEN THE DATE IS NOT PERESENT IN THE DICTIONARY

                            gratuityLi = {}
                            serviceLi = {}
                            refundLi = {}
                            payableLi = {}

                            if gratuity != 0.0:
                                gratuityLi['Gratuity Charge'] = [gratuity]
                            else:
                                gratuityLi['Gratuity Charge'] = []
                            
                            if service != 0.0:
                                serviceLi['Service Charge Rate'] = [service]
                            else:
                                serviceLi['Service Charge Rate'] = []

                            if refund != 0.0:
                                refundLi['Payment Refunded'] = [refund]
                            else:
                                refundLi['Payment Refunded'] = []
                            
                            if payable == 0.0:
                                payableLi['Net Payout Amount'] = []
                            else:
                                payableLi['Net Payout Amount'] = [payable]

                            paymentDetailsLi = [gratuityLi, serviceLi, refundLi, payableLi]

                            experienceDictionary[experience] = paymentDetailsLi

                            transactionsRecord_byDate[date] = [experienceDictionary]

                            continue


                        
                        if transactionsRecord_byDate.get(date, None) != None: #WHEN THE DATE IS PERESENT IN THE DICTIONARY

                            experienceList = transactionsRecord_byDate.get(date)
                            
                            flag = 0

                            for exp in experienceList: # CHECKING IF THE EXPERIENE OF THE ROW IS PRESENT ON THE DATE OF THE ROW
                                if list(exp.keys())[0] == experience:

                                    flag = 1

                                    paymentDetailsLi = list(exp.values())[0]

                                    for pay in paymentDetailsLi:
                                        if list(pay.keys())[0] == 'Gratuity Charge' and gratuity != 0.0:
                                            pay.get('Gratuity Charge').append(gratuity)
                                        if list(pay.keys())[0] == 'Service Charge Rate' and service != 0.0:
                                            pay.get('Service Charge Rate').append(service)
                                        if list(pay.keys())[0] == 'Payment Refunded' and refund != 0:
                                            pay.get('Payment Refunded').append(refund)
                                        if list(pay.keys())[0] == 'Net Payout Amount' and payable != 0:
                                            pay.get('Net Payout Amount').append(payable)
                                        

                                    
                            if flag == 0:

                                if gratuity != 0.0:
                                    gratuityLi['Gratuity Charge'] = [gratuity]
                                else:
                                    gratuityLi['Gratuity Charge'] = []
                                if service != 0.0:
                                    serviceLi['Service Charge Rate'] = [service]
                                else:
                                    serviceLi['Service Charge Rate'] = []
                                if refund != 0.0:
                                    refundLi['Payment Refunded'] =  [refund]
                                else:
                                    refundLi['Payment Refunded'] =  []
                                if payable != 0.0:
                                    payableLi['Net Payout Amount'] = [payable]
                                else:
                                    payableLi['Net Payout Amount'] = []

                                paymentDetailsLi = [gratuityLi, serviceLi, refundLi, payableLi]

                                experienceDictionary[experience] = paymentDetailsLi

                                transactionsRecord_byDate.get(date).append(experienceDictionary)

    transactionsRecord_byDate = OrderedDict(sorted(transactionsRecord_byDate.items()))

    return (transactionsRecord_byDate, expericenceList, dateList)


def createOutputFile(transactionsRecord_byDate, experienceList, dateList, relevantExperiences, tockExperiences):
    
    dateList.sort()

    dataFileDictionary = {} # THIS DICTIONARY WILL HOLD ALL THE EXPERIECNE PER DAY VALUES TOTAL

    finalTable = [] # THE FINAL TABLE WHICH HOLDS THE DATA TO BE WRITTEN ON THE FILE
    finalTablePerExpericence = [] # FINAL TABLE FOR EVERY EXPERIENCE
    experienceRow = []
    fields = ['Row Lables', 'Sum of Gratuity Charge', 'Sum of Service Charge', 'Sum of Payment Refunded', 'Sum of Net Payout Amount']

    finalTablePerExpericence.append(fields)
    flag = 0
    gratuityTockList = []
    listOfgratuityTockList = []

    for exp in experienceList:
        if exp in tockExperiences:
            flag = 1
        if exp in relevantExperiences:
            grandTotalGratuity = 0.0
            grandTotalService = 0.0
            grandTotalRefund = 0.0
            grandTotalPayout = 0.0

            for date, dataList in transactionsRecord_byDate.items():
                for expDic in dataList:
                    if exp == list(expDic.keys())[0]:

                        experienceRow.append(date)
                        paymentList = list(expDic.values())[0]
                        for pays in paymentList:
                            li = list(pays.items())[0][1]
                            experienceRow.append(round(sum(li),4))


                if(len(experienceRow) != 0):
                    grandTotalGratuity += experienceRow[1]
                    grandTotalService += experienceRow[2]
                    grandTotalRefund += experienceRow[3]
                    grandTotalPayout += experienceRow[4] 
                    finalTablePerExpericence.append(experienceRow)
                    if flag == 1:
                        gratuityTockList.append((date,experienceRow[1]))
                experienceRow = []
                
            finalTablePerExpericence.append(['Grand Total',round(grandTotalGratuity,4),round(grandTotalService,4),round(grandTotalRefund,4),round(grandTotalPayout,4)])   
        
            dataFileDictionary[exp] = finalTablePerExpericence
            finalTablePerExpericence = []
            finalTablePerExpericence.append(fields)

            if flag == 1:
                listOfgratuityTockList.append(gratuityTockList)
                gratuityTockList = []
                flag = 0

    #print(listOfgratuityTockList)    

    index = 1
    dateCompleted = []
    
    totalSumTable = []

    grandTotalSumOfGratuity = 0.0
    grandTotalSumOfService = 0.0
    grandTotalSumOfRefund = 0.0
    grandTotalSumOfPayout = 0.0

    #print(dataFileDictionary)

    for date in dateList:
        totalSumOfGratuity = 0.0
        totalSumOfService = 0.0
        totalSumOfRefund = 0.0
        totalSumOfPayout = 0.0
        for exp, listOfrows in dataFileDictionary.items():
            count = 0
            for row in listOfrows:
                if count == 0:
                    count+=1
                    continue
                else:
                    if date == row[0]:
                        totalSumOfGratuity += row[1]
                        totalSumOfService += row[2]
                        totalSumOfRefund += row[3]
                        totalSumOfPayout += row[4]

        grandTotalSumOfGratuity+=totalSumOfGratuity
        grandTotalSumOfPayout+=totalSumOfPayout
        grandTotalSumOfRefund+=totalSumOfRefund
        grandTotalSumOfService+=totalSumOfService
        

            

        totalSumTable.append([date,round(totalSumOfGratuity,4), round(totalSumOfService,4), round(totalSumOfRefund,4), round(totalSumOfPayout,4)])

    totalSumTable.insert(0,['Row Lables', 'Total Sum of Gratuity Charge', 'Total Sum of Service Charge', 'Total Sum of Payment Refunded', 'Total Sum of Net Payout Amount'])
    totalSumTable.append(['GRAND TOTAL',round(grandTotalSumOfGratuity,4), round(grandTotalSumOfService,4), round(grandTotalSumOfRefund,4), round(grandTotalSumOfPayout,4)])
        


    for exp, tablePerExperience in dataFileDictionary.items():
        
        finalTable.append([exp])
        for row in tablePerExperience:
            finalTable.append(row)

        finalTable.append([])
        finalTable.append([])

    for row in totalSumTable:
        finalTable.append(row)


    with open('transactionCalculations.csv', mode='w') as transactions: #WRITING DATA TO THE FILE
        transaction_obj = csv.writer(transactions, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        transaction_obj.writerows(finalTable)

    return listOfgratuityTockList
