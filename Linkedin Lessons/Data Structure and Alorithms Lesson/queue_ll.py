"""
2024 - 5/25
1445 - ذُو ٱلْقَعْدَة - 18

Queue
"""
from collections import deque  # optimized for exertion and deletion for the ends


class Queue:
    def __init__(self):
        self.items = deque()  # constructor for deque

    def is_empty(self):
        return not self.items

    def enqueue(self, item):  # adding item in - right hand side of the deque
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()  # pops the item on the index [0]

    def size(self):
        return  len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):  # string representation
        return str(self.items)


if __name__ == "__main__":
    q = Queue()
    print(q)
    print(q.is_empty())
    q.enqueue("M")  # quick tip: ctrl d, duplicated the code in the line
    q.enqueue("O")
    q.enqueue("Y")
    q.enqueue("4")
    print(q)
    print(q.dequeue())
    print(q)
    print(q.size())
    print(q.peek())
    print(q)

"""
code challenge
my_solution________
def queue_challenge():
    my_queue = Queue()
    word_list = ["wore", "a", "silly", "hat", "the", "aardvark"]
    for word in word_list:
        my_queue.enqueue(word)

    var_1 = my_queue.dequeue()
    var_2 = my_queue.dequeue()
    var_3 = my_queue.dequeue()
    var_4 = my_queue.dequeue()

    my_queue.enqueue(var_1)
    my_queue.enqueue(var_2)
    my_queue.enqueue(var_3)
    my_queue.enqueue(var_4)

    print(my_queue)
"""