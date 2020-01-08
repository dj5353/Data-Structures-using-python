class Node():
    def __init__(self,data):
        self.val  =  data
        self.next = None
class Single_linked_list(l):
    def __init__(self,l):
        self.head = None
        self.l = l
    
    def isPalindrome(self):
        
            if head is None:
                return True
            else:
                list1 = []
                p = head
                while p:
                    list1.append(p.val)
                    p = p.next
                return list1

obj = Single_linked_list(l =[1,2,3,4,5])
print(obj.isPalindrome())

