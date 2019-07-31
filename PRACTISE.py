class Node():
    def __init__(self,val):
        self.info = val
        self.lchild = None
        self.rchild = None

class Binary_search_tree():
    def __init__(self):
        self.root = None

    def insert(self):
        data = int(input("Enter the data"))
        temp = Node(data)
        if self.root is None:
            self.root = temp
        else:
            self._insert(data,self.root)

    def _insert(self,val,cur_data):
        if val< cur_data.info:
            if cur_data.lchild == None:
                cur_data.lchild = Node(val)
            else:
                self._insert(val,cur_data.lchild)
        elif val>cur_data.info:
            if cur_data.rchild == None:
                cur_data.rchild = Node(val)
            else:
                self._insert(val,cur_data.rchild)
        else:
            print("Element is already present in the list")

    def display(self):
        if self.root != None:
            self._display(self.root)

    def _display(self,cur_node):
        if cur_node != None:
            self._display(cur_node.lchild)
            print(cur_node.info)
            self._display(cur_node.rchild)

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self,p):
        if p is None:
            return
        print(p.info," ",end="")
        self._preorder(p.lchild)
        self._preorder(p.rchild)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self,p):

        if p is None:
            return
        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print(p.info," ",end ="")

    def search(self,x):
        if self.root != None:
            self._search(x,self.root)
        else:
            print("Element is not found")

    def _search(self,x,cur_node):
        if x == cur_node.info:
            print("Element found")

        elif x < cur_node.info and cur_node.lchild != None:
            return self._search(x,cur_node.lchild)

        elif x > cur_node.info and cur_node.rchild != None:
            return self._search(x,cur_node.rchild)

        else:
            print("Element is not found")

obj = Binary_search_tree()
obj.insert()
obj.insert()
obj.insert()
obj.insert()
obj.insert()
obj.insert()
(obj.search(2))
