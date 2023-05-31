import pandas as pd

class PointTable:

    def __init__(self):
        
        self.point_table = pd.read_csv('Points Table.csv').drop('Position', axis=1)
        self.point_table_dic = {}
        self.__generatePointTableDic()

    def __generatePointTableDic(self):

        column_names = list(self.point_table.columns)

        points = list(self.point_table.iloc[0])
        tipPool = list(self.point_table.iloc[1])
        gratuityPool = list(self.point_table.iloc[2])
        tipPercent = list(self.point_table.iloc[3])
        gratuityPercent = list(self.point_table.iloc[4])
        processingCharge = list(self.point_table.iloc[5])

        for i in range(len(column_names)):
            
            self.point_table_dic[column_names[i]] = {
                "points" : float(points[i]),
                "tipPool" : tipPool[i],
                "gratuityPool" : gratuityPool[i],
                "tipPercent" : float(tipPercent[i]),
                "gratuityPercent" : float(gratuityPercent[i]),
                "processingCharge" : float(processingCharge[i])
            }