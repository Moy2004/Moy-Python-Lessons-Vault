"""
2022-11-18
1444-رَبِيع ٱلْآخِرَة-24

String Functions
"""

# we can treat string as a sequence of characters

text = "Hello World"

print(text[0])
print(text[6:])

for letter in text:
    print(letter)

"""
Escape Characters 
editing the character sequence

\n = new line
\t = tab 
\b = back space 

and many more exist 
"""

# string formatting
# Inputting the value into the "" or quote

name = "moy"

print("My name is %s" % name)  # have to specify the data type
print("My name is {}".format(name))  # {} = place holder + it can take any data type

# string functions
# create expressions in Access that manipulate text in a variety of ways

text = "we boutta upgrade"

print(text.upper())
print(text.count(" "))  # counts the specific give string. EX in this case it counts how many spaces it has
print(text.find("upgrade"))  # finding the index of specific string

"""
.lower = lower case
.title = Capitalize first letter of every word
.swap = swap the case 
"""

# join function
# add up the sequence using given connector/seperator

connector = " "
mylist = ["Moy", "shoot", "Missile"]

print(connector.join(mylist))

# replace function

text = "we get replace"

print(text.replace("replace", "choco"))

"""
quick 日記
드디어 끝났다 ㅋㅋㅋㅋㅋ
뭐 오늘 포함 12일 이면 나쁘지 않다봄 (막상 일한 날은 6일)
그래도 예전의 비하면 엉청 consistent(지속적) 으로 일해서 
배움이 잘 됬다고 본다 킹아!
"""
