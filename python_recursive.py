class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root: TreeNode) -> TreeNode:
    if root is None:
        return None
    
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

def print_tree(node: TreeNode, level=0, prefix="Root: "):
    if node:
        print("    " * level + prefix + str(node.val))
        print_tree(node.left, level + 1, "L--- ")
        print_tree(node.right, level + 1, "R--- ")

root = TreeNode(1,
    left=TreeNode(2, TreeNode(4), TreeNode(5)),
    right=TreeNode(3)
)

print("Original:")
print_tree(root)

invert_tree(root)

print("\n Inverted:")
print_tree(root)
