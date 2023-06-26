#POST Order Traversal

def postorderTraversal(self, root):
    
        answer = []

        def helper(tree):
            if tree:
                helper(tree.left)
                helper(tree.right)
                answer.append(tree.val)
        
        helper(root)
        return answer