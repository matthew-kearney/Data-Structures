"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""



class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
             if not self.left:
                 self.left = BSTNode(value)
             else:
                 self.left.insert(value)
        else:
             if not self.right:
                 self.right = BSTNode(value)
             else:
                 self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
             return True
        else:
            if target < self.value:
                if not self.left:
                    return False
                if self.left.value == target:
                    return True
                else:
                    self.left.contains(target)
            else: 
                if not self.right:
                    return False
                if self.right.value == target:
                    return True
                else:
                    self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
             return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
             return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = [node]
        while True:
            # print("---------")
            val = q[0]
            print(val.value)
            q.remove(val)
            if val.left:
                q.append(val.left)
            if val.right:
                q.append(val.right)
            if len(q) == 0: break

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node is None:
             return
        print(node.value)
        self.dft_print(node.left)
        self.dft_print(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
