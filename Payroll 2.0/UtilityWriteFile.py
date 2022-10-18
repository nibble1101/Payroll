import csv

class UtilityWriteFile:

    def __init__(self):
        pass

    @staticmethod
    def writeTipsGratuity(tip_dic, gratuity_dic):

        date_col = []
        tip_date = list(tip_dic.keys())
        gratuity_date = list(gratuity_dic.keys())
        print(tip_date == gratuity_date)
        gratuity_date.insert(0," ")

        with open("Tip-Gratuity.csv", "w") as outfile:
 
            # pass the csv file to csv.writer function.
            writer = csv.writer(outfile)
        
            # pass the dictionary keys to writerow
            # function to frame the columns of the csv file
            writer.writerow(gratuity_date)
        
            # make use of writerows function to append
            # the remaining values to the corresponding
            # columns using zip function.
            tipLi = []
            gratuityLi = []
            tips = tip_dic.values()
            gratuities = gratuity_dic.values()

            for tip in tips:
                tipLi.append(list(tip.values())[0])

            for gratuity in gratuities:
                gratuityLi.append(list(gratuity.values())[0])

            tipLi.insert(0,"Tip")
            gratuityLi.insert(0,"Gratuity")

            writer.writerows([tipLi, gratuityLi])



