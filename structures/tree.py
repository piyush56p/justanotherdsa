class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Constructing the tree manually
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Now, `root` is the root of the binary tree.


#Print the tree. preorder traversaldef preorder(node):
def preorder(node):
    if not node:
        return
    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)


    # Print the tree in preorder
preorder(root)
