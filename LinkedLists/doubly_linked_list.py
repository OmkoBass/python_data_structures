class doublyLinked:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, node):
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            node.prev = self.last
            self.last = node
    
    def print(self):
        print("Forward")
        temp = self.first
        while temp is not None:
            print(f"{temp.value} -> ", end = "")
            if(temp.next is None):
                print("VOID")
            temp = temp.next
        print("")
    
    def print_reverse(self):
        print("Reverse")
        temp = self.last
        while temp is not None:
            print(f"{temp.value} -> ", end = "")
            if(temp.prev is None):
                print("VOID")
            temp = temp.prev
        print("")

    def remove(self, value):
        if self.first.value is value:
            deleted = self.first
            self.first = self.first.next
            return deleted

        temp = self.first
        forward = temp.next

        while forward is not None:
            if forward.value is value:
                helper = forward.next
                temp.next = helper
                helper.prev = temp
                return forward

            temp = temp.next
            forward = forward.next
        return None

class node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        return

mylist = doublyLinked()
mylist.add(node("ASDFGH"))
mylist.add(node(0))
mylist.add(node(16))
mylist.add(node(32))
mylist.add(node(48))
mylist.add(node(64))
mylist.add(node("QWERTY"))
mylist.print()
mylist.remove("ASDFGH")
mylist.print()
