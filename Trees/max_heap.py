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

class MaxHeap:
    root = None

    def add(self, newnode):
        if type(newnode) is not Node:
            newnode = Node(newnode)
        
        if self.root is None:
            self.root = newnode
            return
        
        if self.root.left is not None:
            self.root.left.add(newnode)
        
        if self.root.right is not None:
            self.root.right.add(newnode)
        
        self.root.Heapify()
    
    def Heapify(self):
        if self.root.value < self.root.left.value and self.root.left is not None:
            swap(self.root, self.root.left)
            if self.root.value < self.root.right.value and self.root.right is not None:
                swap(self.root, self.root.right)
        
        if self.root.value < self.root.right.value and self.root.right is not None:
            swap(self.root, self.root.right)
            if self.root.value < self.root.left.value and self.root.left is not None:
                swap(self.root, self.root.left)
        
        self.root.left.Heapify()
        self.root.right.Heapify()


    def preorder(self):
        self.root.preorder()
    
    def inorder(self):
        self.root.inorder()
    
    def postorder(self):
        self.root.postorder()

def swap(first_node, second_node):
        first_node, second_node = second_node, first_node


my_heap = MaxHeap()

my_heap.add(Node(6))
my_heap.add(Node(1))
my_heap.add(Node(3))

my_heap.preorder()