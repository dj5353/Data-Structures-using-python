class Node():
    def __init__(self, value):
        self.info = value
        self.next = None

class Linked_list():
    def __init__(self):
        self.head = None

    def display(self):
        current_node = self.head
        if current_node is None:
            print("List is Empty")
        else:
            while current_node:
                print(current_node.info)
                current_node = current_node.next

    def insert_at_end(self,data):
        p = self.head
        if self.head is None:
            temp = Node(data)
            self.head = temp
            return
        else:
            while p.next:
                p = p.next
            temp = Node(data)
            p.next = temp


    def insert_at_beginning(self,data):
        temp = Node(data)
        p = self.head
        temp.next = p
        self.head = temp

    def create_list(self):
        n = int(input("enter how many number of nodes you want to insert"))
        if n == 0:
            return
        else:
            for i in range(n):
                data = input("Enter the data to insert")
                self.insert_at_end(data)

    def insert_before(self):
        pos = input("Enter the number before which you want to insert number")
        data = input("Enter the data")
        p = self.head
        if self.head is None:
            print("list is empty")
            return
        if self.head.info == pos:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
        else:
            while p.next:
                if p.next.info == pos:
                    break
                p = p.next
            if p.next is None:
                print("element is not present in the list")
            else:
                temp = Node(data)
                temp.next = p.next
                p.next = temp

    def insert_after_item(self, x, data):

        p = self.head
        while p is not None:
            if p.info == x:
                break
            p = p.next
        if p is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.next = p.next
            p.next = new_node

    def insert_at_pos(self):
        pos = int(input("Enter the position at which you want to insert new node"))
        data = int(input("Enter the data you want to insert"))
        i = 2
        p = self.head
        if self.head is None:
            print("list is empty")

        if pos == 1:
            temp = Node(data)
            temp.next = self.head
            self.head = temp

        else:
            while p.next is not None:
                if i == pos:
                    break
                p = p.next
                i += 1
            if p.next is None:
                print("pos is out of range")
            else:
                temp = Node(data)
                temp.next = p.next
                p.next = temp

    def delete_first_node(self):
        if self.head is None:
            print("list is already empty")
        else:
            self.head.info = None
            self.head = self.head.next

    def delete_last_Node(self):
        p = self.head
        if self.head is None:
            print("list is empty")
        if self.head.next is None:
            self.head.info = None
        else:
            while p.next.next is not None:
                p = p.next
            p.next = None

    def reverse_list(self):
        p = self.head
        prev = None
        while p:
            next = p.next
            p.next = prev
            prev = p
            p = next
        self.head = prev

    def bubble_sort_exdata(self):
        end = None
        while end != self.head.next:
            p = self.head
            while p.next != end:
                q = p.next
                if p.info > q.info:
                    p.info,q.info = q.info,p.info
                p = p.next
            end = p

    def insert_cycle(self,x):
        if self.head is None:
            return
        p = self.head
        px = None
        prev = None
        while p is not None:
            if p.info == x:
                px = p
            prev = p
            p = p.next
        if px is not None:
            prev.next = px
        else:
            print("Element is not present in the list")
    def has_cycle(self):
        if self.detect_cycle() is None:
            print("Donot have Cycle")
        else:
            print(" have cycle")

    def detect_cycle(self):
        if self.head is None or self.head.next is None:
            return None

        slower = self.head
        faster = self.head
        while faster is not None and faster.next is not None:
            slower = slower.next
            faster = faster.next.next
            if slower == faster:
                return slower
        else:
            return None



obj = Linked_list()
obj.create_list()

while True:
    print("1.Display list")
    print("2.insert at end of the list")
    print("3.insert at beginning of the list")
    print("4.create list")
    print("5.Insert before")
    print("6.Insert after")
    print("7.Insert at pos")
    print("8.Delete First Node")
    print("9.Delete last Node")
    print("10.reverse linked list")
    print("11.sorting list")
    print("12.Insert cycle")
    print("13.Detect Cycle")

    option = int(input("Enter your choice"))

    if option == 1:
        obj.display()

    if option == 2:
        data = input("enter the data you want to insert")
        obj.insert_at_end(data)

    if option == 3:
        data = input("enter the data")
        obj.insert_at_beginning(data)

    if option == 4:
        obj.create_list()

    if option == 5:
        obj.insert_before()

    if option == 6:
        x = int(input("Enter the element after which you want to insert node"))
        data = int(input("enter the data you want to enter"))
        obj.insert_after_item(x,data)

    if option == 7:
        obj.insert_at_pos()

    if option == 8:
        obj.delete_first_node()

    if option == 9:
        obj.delete_last_Node()

    if option == 10:
        obj.reverse_list()

    if option == 11:
        obj.bubble_sort_exdata()

    if option == 12:
        x = int(input("Enter the number from which you want to insert cycle"))
        obj.insert_cycle(x)

    if option == 13:
        obj.has_cycle()
