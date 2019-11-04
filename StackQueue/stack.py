class stack:
    def __init__(self):
        self.nodes = []
    
    def print(self):
        for node in self.nodes:
            print(f"{node}\n", end = "")
    
    def is_empty(self):
        if self.nodes is None:
            return None
    
    def push(self, node):
        self.nodes.append(node)
    
    def pop(self):
        self.nodes = self.nodes[:-1]
    
    def peek(self):
        return self.nodes[len(self.nodes) - 1]
    
mystack = stack()
mystack.push(3)
mystack.push(6)
mystack.pop()
mystack.push(9)
mystack.push(12)
mystack.print()
    