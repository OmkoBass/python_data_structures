class circularList:
    first = None
    last = None
    lenght = 0

    def add(self, to_add):
        if type(to_add) is not node:
            to_add = node(to_add)
        
        if self.first is None:
            self.first = to_add
            self.last = to_add
        else:
            self.last.next = to_add
            self.last = to_add
            self.last.next = self.first
        
        self.lenght += 1
    
    def print(self):
        temp = self.first
        while temp is not self.last:
            print(f'{temp.value} -> ', end = '')
            temp = temp.next
        print(f'{self.last.value} -> {self.first.value}')
    
    def count(self):
        counter = 0
        temp = self.first
        while temp is not self.last:
            counter += 1
            temp = temp.next
        counter += 1
        return counter
    
    def remove(self, searched):
        if self.first.value is searched:
            self.first = self.first.next
            return
        
        temp = self.first

        while temp is not self.last:
            if temp.value == searched:
                temp.value = temp.next.value
                temp.next = temp.next.next
                return
            temp = temp.next
        
        if self.last.value is searched:
            self.last = temp
            temp.next = self.first
            return
    
    def __getitem__(self, index):
        if index < 0 or index >= self.lenght:
            raise IndexError
        
        if index is self.lenght:
            return self.last

        temp = self.first
        i = 0
        while temp is not self.last:
            if i is index:
                return temp.value
            i -= -1 #Haters will say this is stupid B)
            temp = temp.next
        
        return None
    
    def __setitem__(self, index, value):
        if index < 0 or index >= self.lenght:
            raise IndexError
        
        temp = self.first
        i = 0
        while temp is not self.last:
            if i is index:
                temp.value = value
                return
            i += 1
            temp = temp.next
        
        if index is self.lenght:
            self.last.value = value

class node:
    def __init__(self, value):
        self.value = value
        self.next = None
        return
    
    
    def print(self):
        print(self.value)
    

    def __str__(self):
        return str(self.value)
    
mylist = circularList()
mylist.add(node(25))
mylist.add(node(50))
mylist.add(node(75))
mylist.add(node(100))

mylist.print()

print(f'There are {mylist.count()} nodes in our list.')

mylist[2] = 1

mylist.print()