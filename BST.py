class Node():
    def __init__(self, val, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.size  = 0
        self.deep = 0


class binarySearchTree():
    def __init__(self):
        self.root = None
        self.deep = 0
        self.whythisthingevenexists = 0

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, current):
        if val < current.val:
            if current.left == None:
                current.left = Node(val, parent = current)
            else:
                self._insert(val, current.left)
        elif val > current.val:
            if current.right == None:
                current.right = Node(val, parent = current)
            else:
                self._insert(val, current.right)
        else:
            print("no")

    def printTreeInOrder(self):
        if self.root != None:
            self._printTreeInOrder(self.root)
        else:
            print('why')

    def _printTreeInOrder(self, current):
        if current != None:
            self._printTreeInOrder(current.left)
            print(current.val)
            self._printTreeInOrder(current.right)

    def printTreePreOrder(self):
        if self.root != None:
            self._printTreePreOrder(self.root)
        else:
            print('why')

    def _printTreePreOrder(self, current):
        if current != None:
            print(current.val)
            self._printTreePreOrder(current.left)
            self._printTreePreOrder(current.right)

    def printTreePostOrder(self):
        if self.root != None:
            self._printTreePostOrder(self.root)
        else:
            print('why')

    def _printTreePostOrder(self, current):
        if current != None:
            self._printTreePostOrder(current.left)
            self._printTreePostOrder(current.right)
            print(current.val)

    def search(self, val, current):
        if not current:
            print("NO")
        elif val == current.val:
            self.whythisthingevenexists = current
        elif val < current.val:
            self.search(val, current.left)
        elif val > current.val:
            self.search(val, current.right)
            
    def get_size(self):
        if not self.root:
            return
        self.size = self._get_size(self.root)
        print(self.size)
        
    def _get_size(self, node):
        if not node:
            return 0
        else:
            return 1 + self._get_size(node.left) + self._get_size(node.right)

    def get_deep(self, node):
        if not node:
            return 0
        else:
            return 1+max(self.get_deep(node.left), self.get_deep(node.right))

    def get_array(self):
        queue = [self.root]
        res = []
        while queue:
            cell = queue.pop(0)
            res.append(cell.val)
            for i in self.get_adjacent(cell):
                queue.append(i)
        return res
    
    def get_adjacent(self, node):
        a = []
        if node.left:
            a.append(node.left)
        if node.right:
            a.append(node.right)
        return a

    def hasRightChild(self, node):
        self.search(node, self.root)
        return bool(self.whythisthingevenexists.right)

    def hasLeftChild(self, node):
        self.search(node, self.root)
        return bool(self.whythisthingevenexists.left)

    def isRoot(self, node):
        return self.root.val == node

    def hasAnyChildren(self, node):
        self.search(node, self.root)
        return bool(self.whythisthingevenexists.left) or bool(self.whythisthingevenexists.right)

    def hasBothChildren(self, node):
        self.search(node, self.root)
        return bool(self.whythisthingevenexists.left) and bool(self.whythisthingevenexists.right)

    def isLeftChild(self, node):
        self.search(node, self.root)
        return self.whythisthingevenexists.parent.left.val == node
    
    def isRightChild(self, node):
        self.search(node, self.root)
        return self.whythisthingevenexists.parent.right.val == node


p = binarySearchTree()

#for i in range(int(input())):
#    p.insert(int(input()))

#print(p.isRightChild(int(input())))
