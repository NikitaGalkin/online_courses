class MoneyBox:
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity

    def can_add(self, v):
        if ((self.count + v) <= self.capacity):
            return True
        else:
           return False

    def add(self, v):
        self.count += v

x = MoneyBox(15)
if (x.can_add(5)):
    x.add(5)
    print("new is >> " + str(x.count))
if (x.can_add(9)):
    x.add(9)
    print("new is >> " + str(x.count))
if (x.can_add(3)):
    x.add(3)
    print("new is >> " + str(x.count))