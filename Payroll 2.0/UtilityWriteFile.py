import csv

class UtilityWriteFile:

    def __init__(self):
        pass

    @staticmethod
    def writeTipsGratuity(tip_dic, gratuity_dic):
        
        with open("Tip-Gratuity.csv", "w") as outfile:
            
            tipLi = []
            gratuityLi = []

            # pass the csv file to csv.writer function.
            writer = csv.writer(outfile)
        
            # make use of writerows function to append
            # the remaining values to the corresponding
            # columns using zip function.

            # ADDING THE GRATUITY DATES TO THE DATE LIST. THEN WE WILL ADD THE MISSING DATES FROM THE TIP DATES.
            dates = list(gratuity_dic.keys())

            for date in tip_dic.keys():
                if date not in dates:
                    dates.append(date)
            
            # SORTING THE DATES.
            dates.sort()

            tips = tip_dic.values()
            gratuities = gratuity_dic.values()

            # ADD THE MISSING DATES WITH THE VALUE 0
            for date in dates:
                if tip_dic.get(date, None) == None:
                    tip_dic[date] = {"tip":0.0}

                if gratuity_dic.get(date, None) == None:
                    gratuity_dic[date] = {"gratuity":0.0}

            tip_dic= dict(sorted(tip_dic.items(), key=lambda item: item[0]))
            gratuity_dic= dict(sorted(gratuity_dic.items(), key=lambda item: item[0]))

             # ADDING AN EMPTY CELL.
            dates.insert(0," ")

            for tip in tips:
                tipLi.append(list(tip.values())[0])

            for gratuity in gratuities:
                gratuityLi. append(list(gratuity.values())[0])

            tipLi.insert(0,"Tip")
            gratuityLi.insert(0,"Gratuity")

            # pass the dictionary keys to writerow
            # function to frame the columns of the csv file
            writer.writerow(dates)

            writer.writerows([tipLi, gratuityLi])

            return tip_dic,gratuity_dic