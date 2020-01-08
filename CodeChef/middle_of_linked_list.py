class Node():
    def __init__(self,val):
        self.info = val
        self.link = None

    
class Singly_linked():
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
        if self.head is None:
            self.head = Node(data)
        else:
            p = self.head
            while p.link:
                p = p.link
            p.link = Node(data)
    

    def create_Node(self):
        n = int(input("Enter how many nodes you want to create"))
        if n<=0:
            return
        else:
            for i in range(n):
                data = int(input("Enter the Node"))
                self.insert_at_end(data)
                

obj = Singly_linked()
obj.create_Node()
obj.display()
