# exercise for reading and manipulating a csv and excel file
import pandas as pd

index = pd.read_csv("index.csv")

# access 3rd column
column = index.iloc[:, 2:3]
print('\nPrinting the 3rd column')
print(column)

# access last two columns using iloc
column = index.iloc[:, -2:]
print('\nPrinting last two column')
print(column)

# access last 10 rows and first two columns
print('\nPrinting last 10 rows with first two columns')
print(index.iloc[-10:, 0:2])

# sort the table by column I and then by column J
print('\nPrinting the sorted table by first column I and then by column J')
index.sort_values(by=['I', 'J'], ascending=False, inplace=True)
print(index)

# sort the table by index, it would give back the original table
print('\nPrinting the sorted table by index, it would give back the original table')
index.sort_index(inplace=True)
print(index)

