import pandas as pd

point_table = pd.read_csv('Points Table.csv')

# worksheet = gc.open('points-table').sheet1

# get_all_values gives a list of rows.
# rows = worksheet.get_all_values()
# point_table = pd.DataFrame.from_records(rows) 
# column_names = list(point_table.loc[0,:])
print(column_names)
# row_names = list(point_table[0])
# column_names.pop(0)
# row_names.pop(0)
# point_table.drop(0, axis=0, inplace=True)
# point_table.drop(0, axis=1, inplace=True)

# point_table.columns = column_names
# point_table.index = row_names

# point_table_aux = point_table.apply(pd.to_numeric, errors='coerce').fillna(0.0)     # Converting all the values to double type

# global_points_sum = sum(list(point_table_aux.loc["Points"]))

print(point_table)