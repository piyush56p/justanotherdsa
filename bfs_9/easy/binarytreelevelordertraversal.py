import sys
import os

# Add the project root (justanotherdsa) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from structures.tree import TreeNode
from collections import deque

print(TreeNode)

#Level Order traversal
def levelorder(root):
    if root is None:
        return
    queue = deque([root])
    result = []
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_val = queue.popleft()
            current_level.append(current_val.val)
            if current_val.left:
                queue.append(current_val.left)
            if current_val.right:
                queue.append(current_val.right)
        
        result.append(current_level)

print(levelorder(TreeNode.root))
                
