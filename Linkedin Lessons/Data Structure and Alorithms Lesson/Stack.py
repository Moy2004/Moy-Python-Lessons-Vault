"""
2024 - 5/24
1445 - ذُو ٱلْقَعْدَة - 17

Stack
"""


class stack:  # is a blueprint or requirements for be something + constructor creates the object

    def __init__(self):  # Function - Constructor/Method - Parameter(refers to object):
        self.items = []  # these are called attribute + from.what

    def is_empty(self):  # return true if stack is empty
        return not self.items

    def push(self, item):  # add item to the top
        self.items.append(item)

    def pop(self):  # remove item from the top
        return self.items.pop()

    def peek(self):  # return last item on the list
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):  # inspect what is in the stack
        return str(self.items)


if __name__ == "__main__":  # when several files of python, only run this code below when this is the main file
    s = stack()
    print(s)
    print(s.is_empty())
    s.push(3)
    print(s)
    s.push(7)
    s.push(5)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s.size())

"""
Demonstration on code challenge
Answer.py___________________

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)



def reverse_string(my_string):

    reversed_string = ""

    stack = Stack()

    for char in my_string:
        stack.push(char)

    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string


Testing.py_______________

import Answer
test_string = "gninraeL nIdekniL htiw tol a nraeL"
result = Answer.reverse_string(test_string)

"""
