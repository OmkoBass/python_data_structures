class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

    def add(self, newnode):
        if self is not None:
            if newnode.value < self.value:
                if self.left is not None:
                    self.left.add(newnode)
                elif self.left is None:
                    self.left = newnode
            elif newnode.value > self.value:
                if self.right is not None:
                    self.right.add(newnode)
                elif self.right is None:
                    self.right = newnode

    def preorder(self):
        print(f"{self.value} ", end = "")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

root = node(16)
root.add(node(8))
root.add(node(22))
root.preorder()