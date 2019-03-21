# FixSQLDate.py
# Program goes through a text file or csv file and converts DD/MM/YYYY to SQL friendly date format of YYYY-MM-DD
# It changes and corrects the file imported.
# It is fast, a 2 million line csv file is converted in 10 seconds

import re

filename = input("please specify the file name:")

#filename = '/path/to/filename.csv' #you can also write it here, remember to comment out impute line above if you do

def is_date(expression):
    pattern = re.compile('(\d+/\d+/\d+)')
    if pattern.match(expression):
        expression = expression.split('/')
        expression = '-'.join([expression[2],expression[1],expression[0]])
        return expression
    return expression

data = []
with open(filename,'r') as file:
    for line in file.readlines():
        line = line.strip().split('\t')
        for i in range(len(line)):
            line[i]=is_date(line[i])
        data.append('\t'.join(line))
        
with open(filename,'w') as file:
    for line in data:
        file.write(line+'\n')
