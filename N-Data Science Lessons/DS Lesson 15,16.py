"""
2023 2/26
1444 شَعْبَان 6

Pandas Merging, Queries
"""
import pandas as pd

# pandas merging data frames -- Lesson 15
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

# Pandas Queries -- Lesson 16
# csv -- Very popular way to upload or save data set
df = pd.read_csv('people.csv', delimiter=',')  # delimiter == how is it devided
df.set_index('SSN', inplace=True)

print(df.loc[df['Age'] == 45]['Name'])  # getting the Name specifically for people who are 45
print(df.loc[(df['Age'] >= 45) & (df['Height'] > 170)])  # getting entire data of people who meet the requirements

"""
Quick 日記
It is weird, how such a big field
have such a small amount of code
they are prob lot more if we dive in deeper
but still XD
DS Lesson done now time for projects
nice XD
"""


