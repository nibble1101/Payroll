import csv
import datetime
from re import sub

def extractTotalGratuityColumn(finalTableOfSum):

    totalGratuityColumn = {}
    line = 0
    for row in finalTableOfSum:
        if line == 0:
            indexForGratuity = row.index('Total Gratuity')
            indexForDate = row.index('ROW LABELS')
            line+=1
            continue
        else:
            totalGratuityColumn[row[indexForDate]] = row[indexForGratuity]

    return totalGratuityColumn


def createFinalOutputTable(finalHourPerDateTable,totalGratuityColumn, frontHoursTotal, backHoursTotal, timesheetsRecord_byDate, tipPoolDictionary):
    
    line = 0

    gratuitySheetsRecord_byDate = {}

    nameList = []
    
    
    # print(totalGratuityColumn)

    for row in finalHourPerDateTable:
        if line == 0:
            row.append('Total Gratuity')
            line+=1
        else:
            if totalGratuityColumn.get(row[0], None) != None:
                row.append(totalGratuityColumn.get(row[0]))
            else:
                row.append(0.0)


    for date,listOfData in timesheetsRecord_byDate.items():
        for staffRecord in listOfData:
            gratuity = 0.0
            staff_gratuityDict = {}
            name = list(staffRecord.keys())[0]
            if not name in nameList:
                nameList.append(name)
            hours = list(staffRecord.values())[0]
            totalGratuity = totalGratuityColumn.get(date,0.0)
            tipPool = tipPoolDictionary.get(name)
            if tipPool == 10:
                gratuity = hours*(tipPool/100)*totalGratuity/backHoursTotal.get(date)
            elif tipPool == 90:
                gratuity = hours*(tipPool/100)*totalGratuity/frontHoursTotal.get(date)
        
            staff_gratuityDict[name] = round(gratuity,4)
            
            if gratuitySheetsRecord_byDate.get(date,None) == None:
                gratuitySheetsRecord_byDate[date] = [staff_gratuityDict]

            else:
                gratuitySheetsRecord_byDate.get(date).append(staff_gratuityDict)


    #CONVERTING THE DICTIONARY TO TABLE FORM


    nameList.sort()

    fields = nameList
    fields.insert(0,'Dates/Names')

    finalOutputTable = []

    dates = gratuitySheetsRecord_byDate.keys()

    for date in dates:

        row = []
        for i in range(len(fields)):
            row.append(0.0)
        li = gratuitySheetsRecord_byDate.get(date)
        for dicts in li:
            name = list(dicts.keys())[0]
            gratuityTemp = list(dicts.values())[0]
            index = fields.index(name)
            row[index] = gratuityTemp
            
        row[0] = date
        
        finalOutputTable.append(row)

    #print(nameList)

    index = 1
    sumList = []
    for i in range(0,len(nameList)-1): # -1 BECUASE THE NAME LIST ALSO CONATINS DATE/NAMES
        sum = 0
        for row in finalOutputTable:
            if type(row[index]) == float:
                sum+=row[index]
        index+=1
        sumList.append(round(sum,4))
    
    sumList.insert(0,'GRAND TOTAL')
    finalOutputTable.insert(0,fields)
    finalOutputTable.append(sumList)


    return finalOutputTable


    


def findFieldIndex(fields):

    """THIS FUNCTION WILL RETURN THE DICTIONARY WITH THE FIELDS AND THEIR INDEXES IN THE ROWS"""
    
    fieldIndexDictionary = {}
    index = 0

    for field in fields:
        if field == '\ufeffTip' or field == 'Tip':
            fieldIndexDictionary['Tip'] = index
        
        elif field == '\ufeffSubtotal with Tax' or field == 'Subtotal with Tax':
            fieldIndexDictionary['Subtotal with Tax'] = index
        
        elif field == '\ufeffGratuity' or field == 'Gratuity':
            fieldIndexDictionary['Gratuity'] = index

        elif field == '\ufeffBill Date' or field == 'Bill Date':
            fieldIndexDictionary['Bill Date'] = index

        index+=1

    return fieldIndexDictionary


def extractTockExperiences(masterTockExperiences):
    
    """THIS FUNCITON WILL RETURN THE TOCK EXPERIENCES TO BE CALCULATED FROM THE MASTER FILE"""

    tockExperiences = []

    with open(masterTockExperiences, mode='r') as file:
        reader_object = csv.reader(file, delimiter=',')
        line_count = 0

        for row in reader_object:
            if line_count == 0:
                line_count+=1
                continue

            if line_count!=0 and row != []:
                tockExperiences.append(row[0])
    
    return tockExperiences


def outputFile(finalTableOfSum, finalOutputTable):
    with open('paymentDetailsCalculations.csv', mode='w') as outputFile: #WRITING DATA TO THE FILE
        transaction_obj = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        transaction_obj.writerows(finalTableOfSum)
        transaction_obj.writerow([])
        transaction_obj.writerow([])
        transaction_obj.writerow([])
        transaction_obj.writerow([])
        transaction_obj.writerows(finalOutputTable)



def extractData(paymentDetailsSheet, listOfgratuityTockList, tockExperiences):

    """THIS FUNCTION WILL EXTRACT ALL THE DATA AND WILL RETURN THE DICTIONARY"""

    paymentDetails_dictionary = {}
    fieldIndexDictionary = {}
    dateList = []

    with open(paymentDetailsSheet, mode='r') as paymentDetails:
        reader_object = csv.reader(paymentDetails, delimiter=',')
        line_count = 0

        for row in reader_object:
            if line_count == 0:
                fieldIndexDictionary = findFieldIndex(row)
                line_count+=1

            else:
                date_time_str = row[fieldIndexDictionary.get('Bill Date')]
                if date_time_str != '':
                    
                    if row[fieldIndexDictionary.get('Subtotal with Tax')] == '':
                        subTotalWithTax = 0.0 
                    else:
                        subTotalWithTax = round(float(sub(r'[^\d.]', '', row[fieldIndexDictionary.get('Subtotal with Tax')])),4) # EXTRACTING $7.14 FORMAT STRING, THEN EXTRACTING NUMERIC 7.14 FROM $7.14 THEN TURNING THE VALUE TO FLOAT THEN ROUNDING THE VALUE TO 4 PLACES
                        
                    if row[fieldIndexDictionary.get('Gratuity')] == '':
                        gratuity = 0.0
                    else:
                        gratuity = round(float(sub(r'[^\d.]', '', row[fieldIndexDictionary.get('Gratuity')])),4) # EXTRACTING $7.14 FORMAT STRING, THEN EXTRACTING NUMERIC 7.14 FROM $7.14 THEN TURNING THE VALUE TO FLOAT THEN ROUNDING THE VALUE TO 4 PLACES
                    if row[fieldIndexDictionary.get('Tip')] == '':
                        tip = 0.0
                    else:
                        tip = round(float(sub(r'[^\d.]', '', row[fieldIndexDictionary.get('Tip')])),4) # EXTRACTING $7.14 FORMAT STRING, THEN EXTRACTING NUMERIC 7.14 FROM $7.14 THEN TURNING THE VALUE TO FLOAT THEN ROUNDING THE VALUE TO 4 PLACES

                    date = datetime.datetime.strptime(date_time_str, '%m/%d/%y %H:%M').date() 
                    if date not in dateList:
                        dateList.append(date)

                    if paymentDetails_dictionary.get(date,None) == None:
                        paymentDetails_dictionary[date] = [[subTotalWithTax,tip,gratuity]]
                    elif paymentDetails_dictionary.get(date,None) != None:
                        paymentDetails_dictionary.get(date).append([subTotalWithTax,tip,gratuity])
            
    
    countOfTockExperience = len(tockExperiences)

    fields = ['ROW LABELS', 'Sum of Subtotal with Tax', 'Sum of Tip', 'Sum of Gratuity']

    for tockField in tockExperiences:
        str = 'Tock Gratuity ' 
        str += tockField
        fields.append(str)

    fields.append('Total Gratuity')
    finalTableOfSum = []
    finalTableOfSum.append(fields)
    grandTotalOfTotalWithTax = 0.0
    grandTotalOfTotalGratuity = 0.0 
    grandTotalOfTotalTip = 0.0
    grandTotalOfTotalGratuityAfterTock = 0.0

    row = []
    #print(listOfgratuityTockList)
    
    grandTotalsumOfTockGratuityList = [0.0 for i in range(0,countOfTockExperience)]

    for date,listOfData in paymentDetails_dictionary.items():
        vessel = 0.0
        sumOfsubtotalWithTax = 0.0
        sumOfTip = 0.0
        sumOfGratuity = 0.0
        for li in listOfData:
            sumOfsubtotalWithTax+=li[0]
            sumOfTip+=li[1]
            sumOfGratuity+=li[2]


        #CALCULATION NEEDS TO BE DONE ACCORDING TO THE DATES
        index = 0
        row = [date, round(sumOfsubtotalWithTax,4), round(sumOfTip,4), round(sumOfGratuity,4)]
        totalGratuity = 0.0
        for lists in listOfgratuityTockList:
            flag = 0
            for (tockDate, tockGratuity) in lists:
                if date == tockDate:
                    row.append(round(tockGratuity,4))
                    vessel += tockGratuity
                    grandTotalsumOfTockGratuityList[index]+=tockGratuity
                    flag = 1
                    break
            if flag == 0:
                row.append(0.0)
            index+=1
                
        totalGratuity = ((sumOfGratuity + vessel)*0.75 + sumOfTip)*0.95
        row.append(round(totalGratuity,4))
 
        finalTableOfSum.append(row)

            
        grandTotalOfTotalWithTax+=sumOfsubtotalWithTax
        grandTotalOfTotalGratuity+=sumOfGratuity
        grandTotalOfTotalTip+=sumOfTip
        grandTotalOfTotalGratuityAfterTock += totalGratuity                    

    
    row = ['GRAND TOTAL',round(grandTotalOfTotalWithTax,4), round(grandTotalOfTotalTip,4), round(grandTotalOfTotalGratuity,4)]
    for values in grandTotalsumOfTockGratuityList:
        row.append(round(values,4))
    row.append(round(grandTotalOfTotalGratuityAfterTock,4))
    finalTableOfSum.append(row)

    return finalTableOfSum