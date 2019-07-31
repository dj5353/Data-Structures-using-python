class Node():
    def __init__(self,val):
        self.info = val
        self.lchild = None
        self.rchild = None

class Binary_Search_Tree():
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root  == None:
            self.root = Node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,cur_node):
        if value < cur_node.info:
            if cur_node.lchild == None:
                cur_node.lchild = Node(value)
            else:
                self._insert(value,cur_node.lchild)
        elif value > cur_node.info:
            if cur_node.rchild == None:
                cur_node.rchild = Node(value)
            else:
                self._insert(value,cur_node.rchild)
        else:
            print("value already in tree")


    def display(self):
        if self.root != None:
            self._display(self.root)

    def _display(self,cur_node):
        if cur_node != None:
            self._display(cur_node.lchild)
            print("     ",cur_node.info)
            self._display(cur_node.rchild)

    def height(self):
        if self.root != None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self,cur_node,cur_height):
        if cur_node == None: return cur_height
        left_height = self._height(cur_node.lchild,cur_height + 1)
        right_height = self._height(cur_node.rchild,cur_height + 1)
        return max(left_height,right_height)

    def search(self,value):
        if self.root != None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self,value,cur_node):
        if value == cur_node.info:
            return True
        elif value <cur_node.info and cur_node.lchild != None:
            return self._search(value,cur_node.lchild)
        elif value > cur_node.info and cur_node.rchild != None:
            return self._search(value,cur_node.rchild)
        return False

bt = Binary_Search_Tree()
bt.insert(10)
bt.insert(20)
bt.insert(0)
bt.insert(2)
bt.display()
print("Tree height is :",bt.height())
print(bt.search(10))
print(bt.search(20))