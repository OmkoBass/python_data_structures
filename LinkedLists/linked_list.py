class linkedList:
    def __init__(self):
        self.first = None
        self.last = None
        return
    
    def add(self, node):
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
    
    def print(self):
        temp = self.first
        while temp is not None:
            print(f"{temp.value} -> ", end = "")
            if temp.next is None:
                print(f"VOID")
            temp = temp.next
        print("")
    
    def count(self):
        counter = 0
        temp = self.first
        while temp is not None:
            counter += 1
            temp = temp.next
        return counter
    
    def remove(self, searched):
        if self.first.value is searched:
            deleted = self.first
            self.first = self.first.next
            return deleted

        temp = self.first
        forward = temp.next

        while forward is not None:
            if forward.value is searched:
                temp.next = forward.next
                return forward

            temp = temp.next
            forward = forward.next
        return None
    

class node:
    def __init__(self, value):
        self.value = value
        self.next = None
        return
    
    def print(self):
        print(self.value)

mylist = linkedList()
mylist.add(node(50))
mylist.add(node("IceCream"))
mylist.add(node(35))
mylist.add(node("M&M"))
mylist.add(node(20))
mylist.add(node("Skittles"))
mylist.add(node(5))
mylist.print()
mylist.remove(50)
mylist.print()
print(f"There are {mylist.count()} nodes.")