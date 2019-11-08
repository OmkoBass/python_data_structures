class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

    def preorder(self):
        print(f"{self.value} ", end = "")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(f"{self.value} ", end = "")
        if self.right:
            self.right.inorder()
        
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(f"{self.value} ", end = "")
    

class binarytree:
    def __init__(self):
        self.root = None

    def add(self, newnode):
        if newnode is not node:
            node(newnode)

        if self.root is None:
            self.root = newnode
            return
        
        if newnode.value < self.root.value:
            if self.root.left is not None:
                self.root.left.add(newnode)
            elif self.root.left is None:
                self.root.left = newnode
        elif newnode.value > self.root.value:
            if self.root.right is not None:
                self.root.right.add(newnode)
            elif self.root.right is None:
                self.root.right = newnode    

    def preorder(self):
        self.root.preorder()

    def inorder(self):
        self.root.inorder()

    def postorder(self):
        self.root.postorder()
    
    def tree_sum(self):
        self.root.tree_sum()        

mytree = binarytree()

mytree.add(node(16))
mytree.add(node(8))
mytree.add(node(22))

mytree.inorder()

print(mytree.tree_sum())
