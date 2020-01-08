class Base():
    def __init__(self,a,g):
        self._attr = a
        self.get = g
    
class derived(Base):
    def __init__(self,a,g):
        super().__init__(a,g)
        self._attr = 3
        self.age = 19
    
obj2 = Base(1,2)
print(obj2._attr)
print(obj2.get)


obj = derived(1,2)
print(obj.age)
print(obj._attr)
print(obj.get)


