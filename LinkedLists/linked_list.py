class linkedList:
    
    first = None
    last = None
    length = 0
    

    def add(self, to_add):
        if type(to_add) is not node:
            to_add = node(to_add)

        if self.first is None:
            self.first = to_add
            self.last = to_add
        else:
            self.last.next = to_add
            self.last = to_add

        self.length += 1
    

    def print(self):
        temp = self.first
        while temp:
            print(f"{temp.value} -> ", end = "")
            temp = temp.next
        print("nil")
    

    def count(self):
        counter = 0
        temp = self.first
        while temp:
            counter += 1
            temp = temp.next
        return counter
    

    def remove(self, searched):
        if self.first.value == searched:
            self.first = self.first.next
            return
        
        temp = self.first
        
        while temp:
            if temp.value == searched:
                temp.value = temp.next.value
                temp.next = temp.next.next
                return
            temp = temp.next


    def __str__(self):
        out = '['
        temp = self.first
        while temp.next:
            out += str(temp) + ', '
            temp = temp.next
        out += str(temp) + ']'
        return out

    def __iter__(self):
        temp = self.first
        while temp:
            yield temp.value
            temp = temp.next


    def __getitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError

        temp = self.first
        i = 0
        while temp:
            if i == index:
                return temp.value
            i += 1
            temp = temp.next

        return None

    def __setitem__(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError

        temp = self.first
        i = 0
        while temp:
            if i == index:
                temp.value = value
                return
            i += 1
            temp = temp.next



class node:
    def __init__(self, value):
        self.value = value
        self.next = None
        return
    

    def print(self):
        print(self.value)

    
    def __str__(self):
        return str(self.value)


mylist = linkedList()
mylist.add(node(50))
mylist.add(node("IceCream"))
mylist.add(node(35))
mylist.add("M&M")
mylist.add(20)
mylist.add("Skittles")
mylist.add(5)
mylist.print()
mylist.remove(50)
mylist.print()
print(mylist)
print(f"There are {mylist.count()} nodes.")

print("on index 3 is ", mylist[3])
mylist[2] = 1

for element in mylist:
    print(element)

# this should give error
# print(mylist[34])
