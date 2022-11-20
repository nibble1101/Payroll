import pandas as pd

point_table = pd.read_csv('Points Table.csv')
point_table = point_table.drop('Position', axis=1)

# point_table = pd.DataFrame.from_records(rows) 
column_names = list(point_table.columns)
print(column_names)
point_table_dic = {}

points = list(point_table.iloc[0])
tipPool = list(point_table.iloc[1])
gratuityPool = list(point_table.iloc[2])
tipPercent = list(point_table.iloc[3])
gratuityPercent = list(point_table.iloc[4])
processingCharge = list(point_table.iloc[5])

for i in range(len(column_names)):
    
    point_table_dic[column_names[i]] = {
        "points" : float(points[i]),
        "tipPool" : tipPool[i],
        "gratuityPool" : gratuityPool[i],
        "tipPercent" : float(tipPercent[i]),
        "gratuityPercent" : float(gratuityPercent[i]),
        "processingCharge" : float(processingCharge[i])
    }