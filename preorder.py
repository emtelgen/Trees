#PRE Order Tree Traversal

def preorderTraversal(self, root):
        
        answer = []

        def helper(tree):
            if tree:
                answer.append(tree.val)
                helper(tree.left)
                helper(tree.right)
            return answer

        helper(root)
        return answer