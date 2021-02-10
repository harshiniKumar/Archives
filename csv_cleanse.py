import csv
import subprocess
import os
with open(path, newline='') as csvfile:  #path = Path of input file
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    fields=[] # Enter the column headings to be set
    with open('output.csv', 'w', newline='') as csvfile2:
        spamwriter = csv.writer(csvfile2, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        next(csvfile)
        next(csvfile)
        spamwriter.writerow(fields)
        for rows in spamreader:
            spamwriter.writerow(rows)
            print(rows)
