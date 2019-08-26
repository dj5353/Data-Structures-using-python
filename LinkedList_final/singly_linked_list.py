# creating Node class
class Node():
    # Each node has its data and a pointer that points to next node and the previous node in the Linked List
    def __init__(self,val):
        self.info = val
        self.link = None


# creating doubly linked list class
class SingleLinked_list():
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
                p = p.link

    # insert in beginning of doubly linked list
    def insert_in_the_beginning(self, data):
        temp = Node(data)
        temp.link = self.head
        self.head = temp

    # insert in end of doubly linked list
    def insert_at_the_end(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            p = self.head
            while p.link:
                p = p.link
            temp = Node(data)
            p.link = temp

    #creating linked list
    def insert_node(self):
        n = int(input("Enter how many nodes you want to insert"))
        if n == 0:
            return
        else:
            for i in range(n):
                data = int(input("Enter the data you want to enter"))
                self.insert_at_the_end(data)

    # insert new node just after the target node
    def insert_after(self, data):
        x = int(input("Enter the node after which you want to insert"))
        p = self.head
        if x == self.head.info:
            temp = Node(data)
            temp.link = self.head.link
            self.head.link = temp
            return
        else:
            while p:
                if x == p.info:
                    break
                p = p.link
            if p is None:
                print("element is  not present in the list")
            else:
                temp = Node(data)
                temp.link = p.link
                p.link = temp

    # insert new node just before the target node
    def insert_before(self, data):
        x = int(input("Enter the node before which you want to insert element"))
        if x == self.head.info:
            temp = Node(data)
            temp.link = self.head
            self.head = temp
            return
        else:
            p = self.head
            while p:
                if p.link.info == x:
                    break
                p = p.link
            if p is None:
                print("Element is not present in the list")
            else:
                temp = Node(data)
                temp.link = p.link
                p.link = temp

    #insert new node at particular index
    def insert_at_index(self, data):
        count = 2
        x = int(input("Enter the index at which you want to insert"))
        if self.head is None:
            print("List is already empty")
        if x == 1:
            temp = Node(data)
            temp.link = self.head
            self.head = temp
        else:
            p = self.head
            while p.link:
                p = p.link
                count += 1
                if count == x:
                    break
            if p is None:
                print("Index range out of range")
            else:
                temp = Node(data)
                temp.link = p.link
                p.link = temp

    #reversal of linked list
    def reverse_list(self):
        p = self.head
        prev = None
        while p:
            next = p.link
            p.link = prev
            prev =  p
            p = next
        self.head = prev

    #bubble sorting using data exchange method
    def bubble_sort(self):
        end = None
        while end != self.head.link:
            p = self.head
            while p.link !=end :
                q = p.link
                if p.info > q.info:
                    p.info,q.info = q.info,p.info
                p = p.link
            end = p

    #delete node from linked list method
    def delete_node(self):
        n = int(input("Enter the node you want to delete"))

        if self.head is None:
            print("list is already empty")

        if n == self.head.info:
            self.head = self.head.link

        else:
            p = self.head
            while p.link:
                if p.link.info == n:
                    break
                p = p.link
            if p.link is None:
                print("Element is not present in the list")
            else:
                p.link = p.link.link

    #inserting cycle or loop in linked list
    def insert_cycle(self):
        x = int(input("Enter the node at which you want to insert cycle"))
        if self.head is None:
            print("You cannot insert cycle")
            return
        if self.head.info == x:
            p = self.head
            while p.link:
                p = p.link
            if p.link is None:
                p.link = self.head
                self.head = self.head
        else:
            px = None
            p = self.head
            while p.link:
                if p.link.info == x:
                    px = p.link
                p = p.link
            if p.link is None:
                p.link = px

    #has_cycle method to call check_cycle method
    def has_cycle(self):
        if self.check_cycle():
            print("List has cycle in it")
        else:
            print("No cycle present there")

    #To chcck if linked list have cycle(loop) in it
    def check_cycle(self):
        if self.head is None or self.head.link is None:
            return None
        tortoise = self.head
        hare = self.head
        while hare is not None and hare.link is not None:
            tortoise = tortoise.link
            hare = hare.link.link
            if tortoise == hare:
                return tortoise
                break
        else:
            return None
    #hare and tortoise algorithim to find the starting point of loop
    def start_of_loop(self):
        if self.head is None:
            print("list is Empty")
            return
        tortoise = self.head
        hare = self.head
        tortoise = tortoise.link
        hare = hare.link.link
        while hare is not None and hare.link is not None:
            if tortoise == hare:
                break
            tortoise = tortoise.link
            hare = hare.link.link
        tortoise = self.head
        while(tortoise != hare):
            hare = hare.link
            tortoise = tortoise.link
        return tortoise.link.info

    # remove cycle(loop) from linked list and counting length of linked list
    def remove_loop(self):
        c = self.check_cycle()
        print(c.info)
        if c is None:
            print("length of list is 0")
            return
        p = c
        q = c
        len_cycle = 0
        while True:
            p = p.link
            len_cycle += 1
            if p == q:
                break
        print("Length of cycle is {} ".format(len_cycle))
        p = self.head
        q = c
        rem_list = 0
        while True:
            if p == q:
                break
            q = q.link
            p = p.link
            rem_list += 1
        print("Length of list without cycle {}".format(rem_list))
        total_length = len_cycle+rem_list
        print("Total length of list {}".format(total_length))
        p = self.head
        for i in range(total_length-1):
            p = p.link
        p.link = None






obj = SingleLinked_list()
obj.insert_node()
while True:
    print("1.display_list")
    print("2.insert_at_beginning")
    print("3.insert_at_end")
    print("4.insert_after")
    print("5.insert_before")
    print("6.Insert at index")
    print("7.Reverse list")
    print("8.sort list")
    print("9.delete Node")
    print("10.detect cycle")
    print("11.Insert cycle")
    print("12.remove cycle")
    print("13.start of loop")
    print("14.length of cycle")

    option = int(input("Enter your choice"))

    if option == 1:
        obj.display()
    if option == 2:
        data = int(input("Enter the data"))
        obj.insert_in_the_beginning(data)
    if option == 3:
        data = int(input("Enter the data"))
        obj.insert_at_the_end(data)
    if option == 4:
        data = int(input("Enter the data"))
        obj.insert_after(data)
    if option == 5:
        data = int(input("enter the data"))
        obj.insert_before(data)
    if option == 6:
        data = int(input("Enter the data you want ton enter"))
        obj.insert_at_index(data)
    if option == 7:
        obj.reverse_list()
    if option == 8:
        obj.bubble_sort()
    if option == 9:
        obj.delete_node()
    if option == 10:
        obj.has_cycle()
    if option == 11:
        obj.insert_cycle()
    if option == 13:
        print(obj.start_of_loop())
    if option == 14:
        (obj.remove_loop())