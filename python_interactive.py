"""
Lógica da versão iterativa (BFS)

1. Comece com a raiz na fila.
2. Enquanto a fila não estiver vazia:
    - Remova o primeiro nó da fila.
    - Inverta seus filhos esquerdo e direito
    - Adicione os filhos (se existirem) à fila.
3. Retorne a raíz ao fnal.
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree_iterative(root: TreeNode) -> TreeNode:
    if root is None:
        return None
    
    queue = deque([root])

    while queue:
        node = queue.popleft()

        node.left, node.right = node.right, node.left

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

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

print("Original (BFS):")
print_tree(root)

invert_tree_iterative(root)

print("\n Inverted (BFS):")
print_tree(root)
