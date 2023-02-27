"""
2023 2/26
1444 شَعْبَان 6

Pandas Merging data frames
"""
import pandas as pd

# pandas merging data frames
names = {
    'SSN': [1, 2, 4, 7, 8],
    'Name': ['JonJon', 'Ben', 'Dylan', 'Mark', 'Leland']
}

ages = {
    'SSN': [5, 6, 7, 8, 9],
    'Age': [28, 29, 26, 28, 27]
}

DF1 = pd.DataFrame(names)
DF2 = pd.DataFrame(ages)

df = pd.merge(DF1, DF2, on='SSN', how='outer')  # code to merge (DF1,DF2, Which is Column?, Method)
print(df)

"""
There is 4 different ways to merge the data frame

left  join - This type of join returns all the rows from that is mentioned first
inner join - This type of join returns only the matching rows between the two data frames. (Exclude)
outer join - This type of join returns only the matching rows between the two data frames. (Show but as NAN or NULL)
right join - This type of join returns all the rows from that is mentioned secondly

- Help from ChatGPT
"""

