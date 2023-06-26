#MIN Depth of a Binary Tree

def minDepth(tree):
    if tree:
        if not tree.left and not tree.right:
            return 1
        if not tree.left:
            return minDepth(tree.right) + 1
        elif not tree.right:
            return minDepth(tree.left) + 1
        else:
            return min(minDepth(tree.left), minDepth(tree.right)) + 1
    return 0

