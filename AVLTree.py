class Node():
    def __init__(self, val, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.height = 1


class AVLTree():
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)
        
    def _insert(self, node, val):
        if not node:
            return Node(val)
        if val < node.val:
            left = self._insert(node.left, val)
            node.left = left
            left.parent = node
        elif val > node.val:
            right = self._insert(node.right, val)  
            node.right = right
            right.parent = node
        else:
            return node 

        node.height = self.height(node)
        return self.balance(node) 


    def height(self, node):
        if not node:
            return 0
        else:
            return 1+max(self.height(node.left), self.height(node.right))

    def balance(self, node):
        bal = self.get_bal(node)
        if bal == 2:
            if self.get_bal(node.left) <= 0:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        elif bal == -2:
            if self.get_bal(node.right) >= 0:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        else:
            return node

    def get_bal(self, node):
        left = 0
        right = 0
        if node.left:
            left = node.left.height
        if node.right:
            right = node.right.height

        return left - right

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

    def right_rotate(self, node):
        a = node.left
        b = a.right
        a.right = node
        node.left = b

        node.height = self.height(node)
        a.height = self.height(a)

        return a

    def left_rotate(self, node):
        a = node.right
        b = a.left
        
        a.left = node
        node.right = b
        
        node.height = self.height(node)
        a.height = self.height(a)
        
        return a
    
    def printTreePreOrder(self,root):
        if root != None:
            self._printTreePreOrder(root)
        else:
            print('why')

    def _printTreePreOrder(self, current):
        if current != None:
            print(current.val)
            self._printTreePreOrder(current.left)
            self._printTreePreOrder(current.right)

    def _printTreeInOrder(self, current):
        if current != None:
            self._printTreeInOrder(current.left)
            print(current.val)
            self._printTreeInOrder(current.right)


p = AVLTree()
'''
for i in range(int(input())):
    p.insert(int(input()))


print(p.root.val)
'''
