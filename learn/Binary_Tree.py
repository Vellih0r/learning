class BuildNode:
    # class for building nodes
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        left = self.left.val if self.left else None
        right = self.right.val if self.right else None
        return f"{self.val}: Left={left}, Right={right}"

class Tree:
    # class for binary tree
    def __init__(self, root=None):
        self.root = root

    def insert(self, val, node=None):
        # create root and exit
        if self.root is None:
            self.root = BuildNode(val)
            print(f"Inserted root: {self.root}")
            return

        # if no current node -> current node is root
        if node is None:
            node = self.root

        if val < node.val:
            if node.left is None:
                node.left = BuildNode(val)
                print(f"Inserted {val} to left of {node.val}")
            else:
                self.insert(val, node.left)

        else:  # we don't need `>=`, just `else`
            if node.right is None:
                node.right = BuildNode(val)
                print(f"Inserted {val} to right of {node.val}")
            else:
                self.insert(val, node.right)

    def display_tree(self, node=None):
        # Print the tree in an in-order traversal (left, root, right)
        if node is None:
            node = self.root

        if node.left:
            self.display_tree(node.left)
        
        print(node)

        if node.right:
            self.display_tree(node.right)

# Testing the tree
obj = Tree()
obj.insert(5)
obj.insert(10)
obj.insert(4)
obj.insert(6)
obj.insert(11)
obj.insert(3)

print("\nDisplaying Tree:")
obj.display_tree()
