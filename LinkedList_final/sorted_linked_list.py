# creating Node class
class Node():
    # Each node has its data and a pointer that points to next node and the previous node in the Linked List
    def __init__(self, val):
        self.info = val
        self.link = None


# creating doubly linked list class
class Sorted_linked_list():
    #defining head of the doubly linked list
    def __init__(self):
        self.head = None

    #displaying data in the linked list
    def display(self):
        if self.head is None:
            print("List is already empty")
        else:
            p = self.head
            while p:
                print(p.info,end= " ")
                p = p.link

    #inserting new node (sorted format)
    def insert_in_between(self, data):
        temp = Node(data)
        if self.head is None or data < self.head.info:
            temp.link = self.head
            self.head = temp
            return
        else:
            temp = Node(data)
            p = self.head
            while p.link is not None and p.link.info <= data:
                p = p.link
            temp.link = p.link
            p.link = temp

    # creating sorted linked list
    def create_list(self):
        n = int(input("How many nodes you want to enter"))
        if n == 0:
            return
        else:
            for i in range(n):
                data = int(input("Enter the data you want to enter"))
                self.insert_in_between(data)

obj = Sorted_linked_list()
obj.create_list()
while True:
    print("1.display list")

    option = int(input("Enter your choice"))

    if option == 1:
        obj.display()

