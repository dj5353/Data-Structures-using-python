class Node():
    def __init__(self, val):
        self.info = val
        self.lchild = None
        self.rchild = None


class Binary_Tree():
    def __init__(self, val):
        self.root = Node(val)
        self.l = []

    def preorder(self):#NLR
        return self.__preorder(self.root)

    def __preorder(self, p):
        if p is None:
            return
        print(p.info)
        self.__preorder(p.lchild)
        self.__preorder(p.rchild)

    def inorder(self):
        return self.__inorder(self.root)

    def __inorder(self,p):#LNR
        if p is None:
            return
        self.__preorder(p.lchild)
        print(p.info)
        self.__preorder(p.rchild)

    def postorder(self):#LRN
        return self.__postorder(self.root)

    def __postorder(self, p):
        if p is None:
            return
        self.__postorder(p.lchild)
        self.__postorder(p.rchild)
        print(p.info)

    def height(self):
        return self.__height(self.root,0)

    def __height(self, p, cur_height):
        if p is None:return 0
        l_height = self.__height(p.lchild, cur_height+1)
        r_height = self.__height(p.rchild, cur_height+1)

        print(max(l_height,r_height))
        
    def sumNumbers(self):
        self.__sumNumbers(root)
        return self.l
    
    def __sumNumbers(self,cur_pos):
        if cur_pos is None:
            return
        self.l.append(cur_pos.val)
        self.__sumNumbers(cur_pos.left)


obj = Binary_Tree(1)
obj.root.lchild = Node(2)
obj.root.rchild = Node(3)
obj.root.lchild.lchild = Node(4)
obj.root.rchild.rchild = Node(5)
obj.sumNumbers()

'''
while True:
    print("1.Inorder Traversal")
    print("2.preorder Traversal")
    print("3.postorder Traversal")
    print("4.height of Binary Tree")

    option = int(input("Enter the choice"))

    if option == 1:
        obj.inorder()
    if option == 2:
        obj.preorder()
    if option == 3:
        obj.postorder()
    if option == 4:
        obj.height()

'''


