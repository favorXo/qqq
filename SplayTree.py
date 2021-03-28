class Node():
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.height = 1


class SplayTree():
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        left, right = self.split(root, key)
        root = Node(key, left, right)
        self.keep_parent(root)
        self.root = root

    
    def split(self, root, key):
        if root == None:
            return None, None
        root = self.search(key, root)

        if root.value == key:
            self.set_parent(root.left, None)
            self.set_parent(root.right, None)
            return root.left, root.right
        if root.value < key:
            right, root.right = root.right, None
            self.set_parent(right, None)
            return root, right
        else:
            left, root.left = root.left, None
            self.set_parent(left, None)
            return left, root

    def splay(self, node):
        if node.parent == None:
            return node
        parent = node.parent
        root = parent.parent
        if root == None:
            self.rotate(parent, node)
            return node
        else:
            if (root.left == parent) == (parent.left == node):
                self.rotate(root, parent)
                self.rotate(parent, node)
            else:
                self.rotate(parent, node)
                self.rotate(root, node)
            return self.splay(node)
    
    def rotate(self, parent, node):
        root = parent.parent
        if root != None:
            if root.left == parent:
                root.left = node
            else:
                root.right = node

        if parent.left == node:
            parent.left, node.right = node.right, parent
        else:
            parent.right, node.left = node.left, parent

        self.keep_parent(node)
        self.keep_parent(parent)
        node.parent = root

    def set_parent(self, node, parent):
        if node != None:
            node.parent = parent

    def keep_parent(self, node):
        self.set_parent(node.left, node)
        self.set_parent(node.right, node)

    def search(self, value, node):
        if not node:
            print("NO")
            return
        elif value == node.value:
            return self.splay(node)
        elif value < node.value and node.left:
            return self.search(value, node.left)
        elif value > node.value and node.right:
            return self.search(value, node.right)
        return self.splay(node)

    def printTreePreOrder(self, current):
        if current != None:
            print(current.value, end=" ")
            self.printTreePreOrder(current.left)
            self.printTreePreOrder(current.right)

    def printTreeInOrder(self, current):
        if current != None:
            self.printTreeInOrder(current.left)
            print(current.value)
            self.printTreeInOrder(current.right)


p = SplayTree()
root = None
p.insert(p.root, 100)
p.insert(p.root, 50)
p.insert(p.root, 200)
p.insert(p.root, 40)
p.insert(p.root, 30)
p.insert(p.root, 20)
p.insert(p.root, 25)
p.printTreePreOrder(p.root) # 25 20 30 40 50 100 200
p.root = p.search(200, p.root)
print()
p.printTreePreOrder(p.root) # 200 30 25 20 50 40 100 
print()
print(p.root.value)
print(p.root.left.value)
