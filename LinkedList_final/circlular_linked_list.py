# creating Node class
class Node():
    # Each node has its data and a pointer that points to next node and the previous node in the Linked List
    def __init__(self, val):
        self.info = val
        self.link = None


# creating circular linked list class
class Circular_linked_list():
    #defining last node of the doubly linked list(easy to get link to last and first node in circular linked list)
    def __init__(self):
        self.last = None

    # displaying data in the linked list
    def display(self):
        if self.last is None:
            return
        else:
            p = self.last.link
            while True:
                print(p.info)
                p = p.link
                if p == self.last.link:
                    break

    # insert in beginning of circular linked list
    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp

    # insert in end of circular linked list
    def insert_in_end(self, data):
        temp = Node(data)
        if self.last is None:
            self.last = temp
        temp.link = self.last.link
        self.last.link = temp
        self.last = temp

    # create circular linked list
    def create_list(self):
        n = int(input("Enter the number of nodes you want to create"))
        if n <= 0:
            return
        else:
            for i in range(n):
                data = int(input("Enter the data"))
                self.insert_in_end(data)


obj = Circular_linked_list()
obj.create_list()
while True:
    print("1.Display")
    print("2.insert in beginning")
    print("3.insert in end")

    option = int(input("Enter you choice"))

    if option == 1:
        obj.display()
    if option == 2:
        data = int(input("Enter the data"))
        obj.insert_in_beginning(data)
    if option == 3:
        data = int(input("Enter the data"))
        obj.insert_in_end(data)
