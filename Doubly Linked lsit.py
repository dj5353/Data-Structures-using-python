class Node():
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.info = val

class Linked_list():
    def __init__(self):
        self.head = None

    def display_list(self):
        p = self.head
        if self.head is None:
            print("List is Empty")
        else:
            while p:
                print(p.info)
                p = p.next

    def insert_at_first(self,data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            temp = Node(data)
            temp.next = self.head
            self.head.prev = temp
            self.head =temp

    def insert_at_end(self,data):
        temp = Node(data)
        p = self.head
        if self.head is None:
            self.head = temp
        else:
            while p.next :
                p = p.next
            if p.next is None:
                temp.prev = p
                p.next = temp

    def create_list(self):
        n = int(input("Enter how many nodes you want to enter"))
        if n == 0:
            return
        else:
            for i in range(n):
                data = int(input("Enter the data"))
                self.insert_at_end(data)

    def reverse_list(self):
        p1 = self.head
        p2 = p1.next
        p1.next = None
        p1.prev = p2
        while p2:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev
        self.head = p1

    def insert_before_node(self):
        insert = int(input("Enter the node before which you want ot insert"))
        data = int(input("Enter the node you want ot insert"))
        if self.head is None:
            print("list is empty")
            return
        if self.head.info == insert:
            self.insert_at_first(data)
        p = self.head
        while p:
            if p.info == insert:
                break
            p = p.next
        if p is None:
            print("Element is not present in the list")
        else:
            temp = Node(data)
            temp.prev = p.prev
            temp.next = p
            p.prev.next = temp
            p.prev = temp

    def insert_after_node(self):
        insert = int(input("Enter the node before which you want ot insert"))
        data = int(input("Enter the node you want ot insert"))
        if self.head is None:
            print("list is empty")
            return
        p = self.head
        while p:
            if p.info == insert:
                break
            p = p.next
        if p.info is None:
            print("{} not present in the list".format(insert))
        if p.info == insert and p.next is None:
            temp = Node(data)
            p.next = temp
        else:
            temp = Node(data)
            temp.prev = p
            temp.next = p.next
            p.next.prev = temp
            p.next = temp

    def delete_first_node(self):
        self.head = self.head.next

    def delete_last_node(self):
        p = self.head
        while p.next:
            p = p.next
        p.prev.next = None




obj = Linked_list()
obj.create_list()
while True:
    print("1.Display list")
    print("2.Insert at first")
    print("3.Insert at end")
    print("4.Reverse list")
    print("5.Insert before a node")
    print("6.Insert after a node")
    print("7.Delete First Node")
    print("8.Delete last Node")

    option = int(input("Enter your choice"))

    if option == 1:
        obj.display_list()

    if option == 2:
        data = int(input("Enter the data you want to enter"))
        obj.insert_at_first(data)

    if option == 3:
        data = int(input("Enter the data"))
        obj.insert_at_end(data)

    if option == 4:
        obj.reverse_list()

    if option == 5:
        obj.insert_before_node()

    if option == 6:
        obj.insert_after_node()

    if option == 7:
        obj.delete_first_node()

    if option == 8:
        obj.delete_last_node()