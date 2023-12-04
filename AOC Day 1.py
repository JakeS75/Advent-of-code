import pandas as pd

with open('Day 1 puzzle input') as f:
    Input = [line.strip() for line in f.readlines()]

#df = pd.DataFrame(Input)

data = {
    'input values':['1abc2','pqr3stu8vwx','a1b2c3d4e5f','treb7uchet']
}

df = pd.DataFrame(data)

for row in rows:
    digits = [char for char in df if char.isdigit()]
    if len(digits) == 1:

