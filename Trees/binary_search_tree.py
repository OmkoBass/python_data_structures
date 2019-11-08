class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

    def preorder(self):
        print(f"{self.value} ", end="")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(f"{self.value} ", end="")
        if self.right:
            self.right.inorder()
        
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(f"{self.value} ", end="")

    def tree_sum(self):
        t_sum = self.value
        if self.left:
            t_sum += self.left.tree_sum()
        if self.right:
            t_sum += self.right.tree_sum()
        return t_sum


class BinaryTree:
    root = None

    def add(self, newnode):
        if type(newnode) is not Node:
            newnode = Node(newnode)

        if self.root is None:
            self.root = newnode
            return
        
        if newnode.value < self.root.value:
            if self.root.left:
                self.root.left.add(newnode)
            else:
                self.root.left = newnode
        elif newnode.value > self.root.value:
            if self.root.right:
                self.root.right.add(newnode)
            else:
                self.root.right = newnode    

    def preorder(self):
        self.root.preorder()

    def inorder(self):
        self.root.inorder()

    def postorder(self):
        self.root.postorder()
    
    def tree_sum(self):
        return self.root.tree_sum()


mytree = BinaryTree()

mytree.add(Node(16))
mytree.add(Node(8))
mytree.add(22)

mytree.inorder()

print(mytree.tree_sum())
