from datetime import date
import csv

dt = date.today()
dt = dt.strftime("%m/%d/%Y")
print(dt)

filename = "expensetracker.csv"

exp = []
stopped = False
with open(filename, 'w') as file:
    csvwriter = csv.writer(file)
    while not stopped:
        xp = int(input("What is the expense (type 0 to stop): "))
        if xp==0:
            stopped = True
        else:
            csvwriter.writerow([dt, xp])



