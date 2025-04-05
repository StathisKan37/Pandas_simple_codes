import pandas as pd

# Importing the csv file 'Datas_1_Cars.csv'
dataframe = pd.read_csv('Datas_1_Cars.csv')
print('Data Frame:')
print(dataframe)

print('----------------------------------------------')

# Grapping the first 5 rows
print('5 FIRST ROWS:\n')
print(dataframe.head(5))

print('----------------------------------------------')

# Grapping the last 5 rows
print('5 LAST ROWS:\n')
print(dataframe.tail(5))

print('----------------------------------------------')

# Getting info about the dataframe
print('DATAFRAME INFO:\n')
print(dataframe.info())

print('----------------------------------------------')

# Getting the shape of the dataframe
print('DATAFRAME SHAPE:', dataframe.shape)

# Getting number of dimensions of the dataframe
print('DATAFRAME DIMENSIONS:', dataframe.ndim)

print('----------------------------------------------')

# Getting the column dataTypes
print('COLUMNS DATATYPES:\n')
print(dataframe.dtypes)

print('----------------------------------------------')

# Getting the statistics of the dataframe
print('DATAFRAME STATISTICS:\n')
print(dataframe.describe())

print('----------------------------------------------')

# Getting the statistics of a single column
print('BRAND COLUMN STATISTICS:\n')
print(dataframe['Brand'].describe())

print('----------------------------------------------')

# Getting a single column
print('BRAND COLUMN:\n')
print(dataframe['Brand'])
