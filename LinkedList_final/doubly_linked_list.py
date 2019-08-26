# creating Node class
class Node():
    # Each node has its data and a pointer that points to next node and the previous node in the Linked List
    def __init__(self, val):
        self.info = val
        self.next = None
        self.prev = None


# creating doubly linked list class
class Doubly_linked_list():
    #defining head of the doubly linked list
    def __init__(self):
        self.head = None

    # displaying data in the linked list
    def display(self):
        if self.head is None:
            print("List is Empty")
        else:
             p = self.head
             while p:
                 print(p.info)
                 p = p.next

    # insert in beginning of doubly linked list
    def insert_at_beginning(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    # insert in end of doubly linked list
    def insert_at_end(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = temp
            temp.prev = p

    # insert node just after the target node
    def insert_after_node(self, data):
        temp = Node(data)
        x = int(input("Enter the node after which you want to enter"))
        if self.head is None:
            return
        if self.head.info == x:
            temp.next = self.head.next
            self.head.next = temp
            temp.prev = self.head
            self.head.next.prev = temp

        else:
            p = self.head
            while p:
                if p.info == x:
                    break
                p = p.next
            if p is None:
                print("Element is not present in the list")
            else:
                temp = Node(data)
                temp.next = p.next
                p.next = temp
                temp.prev = p
                p.next.prev = temp

    # insert just before the target node
    def insert_before_node(self, data):
        temp = Node(data)
        x = int(input("Enter the node before which you want to insert data"))
        if self.head is None:
            return
        if self.head.info == x:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
        else:
            p = self.head
            while p:
                if p.next.info == x:
                    break
                p = p.next
            if p is None:
                print("Element is not present in the list")
            else:
                temp = Node(data)
                temp.next = p.next
                p.next = temp
                p.next.prev = temp
                temp.prev = p

    # delete first node of doubly linked list
    def delete_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.head.prev = None

    # delete last node of doubly linked list
    def delete_last_node(self):
        if self.head is None:
            return
        else:
            p = self.head
            while p.next:
                p = p.next
            p.prev.next = None

    # delete the target node
    def delete_in_between(self):
        x = int(input("Enter the data you want to delete"))
        if self.head is None:
            return
        if self.head.info == x:
            self.delete_first_node()
        else:
            p = self.head
            while p:
                if p.info == x:
                    break
                p = p.next
            if p is None:
                print("Element is not present in the list")
            else:
                p.prev.next = p.next

    # reverse doubly linked list
    def reverse_list(self):
        p1 = self.head
        p2 = p1.next
        p1.next = None
        p1.prev = p2

    # create doubly linked list
    def create_list(self):
        n = int(input("Enter the number of nodes you want to enter"))
        if n <= 0:
            return
        else:
            for i in range(n):
                data = int(input("Enter the data you want to enter"))
                self.insert_at_end(data)

obj = Doubly_linked_list()
obj.create_list()

while True:
    print("1.Display list")
    print("2.Insert at beginning")
    print("3.Insert at the end")
    print("4.Insert after node")
    print("5.Insert before node")
    print("6.Delete first node")
    print("7.Delete last node")
    print("8.Delete in between ")

    option = int(input("Enter your choice"))

    if option == 1:
        obj.display()
    if option == 2:
        data = int(input("Enter the data"))
        obj.insert_at_beginning(data)
    if option == 3:
        data = int(input("Enter the data"))
        obj.insert_at_end(data)
    if option == 4:
        data = int(input("Enter the data"))
        obj.insert_after_node(data)
    if option == 5:
        data = int(input("Enter the data"))
        obj.insert_before_node(data)
    if option == 6:
        obj.delete_first_node()
    if option == 7:
        obj.delete_last_node()
    if option == 8:
        obj.delete_in_between()