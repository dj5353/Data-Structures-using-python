class Node():
    def __init__(self,data):
        self.link = None
        self.info = data

class Linkedlist():
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            return
        else:
            p = self.head 
            while p:
                print(p.info)
                p = p.link
        
    def insert_at_end(self,data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            p = self.head
            while p.link:
                p = p.link
            p.link = temp
    
    def create_list(self):
        n = int(input("Enter the number of nodes you want to create"))
        if n == 0:
            return
        else:
            for i in range(n):
                data = int(input("Enter the data"))
                self.insert_at_end(data)
            
    def middle_Of_linkedlist(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.link is not None:
            slow = slow.link
            fast = fast.link.link
        return (slow.info)

    def delete_middle(self):
        mid = self.middle_Of_linkedlist()
        p = self.head
        while p:
            if p.link.info == mid:
                break
            p = p.link
        p.link = p.link.link

    def remove_duplicate(self):
        p = p1 = self.head
        p2 = self.head.link
        while p2 is not None and p2.link is not None:
            if p1.info == p2.info:
                p1.link = p1.link.link
                p2 = p2.link
            else:
                p1 = p1.link
                p2 = p2.link

    def detect_loop(self):
        p = self.head
        slow = self.head
        fast = self.head
        while fast is not None and fast.link is not None:
            slow = slow.link
            fast = fast.link.link
            if fast == slow:
                return fast
                break
        else:
            return False
        
    def start_loop(self):
        c = self.detect_loop()
        start = self.head
        while c != start:
            c = c.link
            start = start.link
        return (start.info)

    def remove_loop(self):
        pass

    def insert_cycle(self):
        n = int(input("Enter the node at which you want to insert cycle"))
        p = self.head
        px = None
        if self.head is None:
            return
        while p.link:
            if (p.link.info == n):
                px = p.link
            p = p.link
        if p.link is None:
            p.link = px
        else:
            print("Element is not present in the list")

    def reverse_linked_list(self):
        start = self.head


obj = Linkedlist()
while True:
    print("1.display")
    print("2.insert_At_end")
    print("3.create_list")
    print("4.middle_linked_list")
    print("5.delte_middle")
    print("6.remove duplicates")
    print("7.detect loop")
    print("8.insert cycle")
    print("9.start of loop")

    option = int(input("Enter the choice"))

    if option == 3:
        obj.create_list()
    if option == 1:
        obj.display()
    if option == 2:
        obj.insert_at_end()
    if option == 4:
        print(obj.middle_Of_linkedlist())
    if option == 5:
        obj.delete_middle()
    if option == 6:
        obj.remove_duplicate()
    if option == 7:
        print(obj.detect_loop())
    if option == 8:
        obj.insert_cycle()
    if option == 9:
        print(obj.start_loop())


