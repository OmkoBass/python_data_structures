class queue:
    def __init__(self):
        self.nodes = []
    
    def print(self):
        for node in self.nodes:
            print(f"{node} ", end = "")
    
    def is_empty(self):
        if self.nodes is None:
            return None

    def enque(self, node):
        self.nodes.append(node)
    
    def deque(self):
        self.nodes = self.nodes[1:]

myqueue = queue()
myqueue.enque(6)
myqueue.deque()
myqueue.enque(12)
myqueue.enque(18)
myqueue.print()