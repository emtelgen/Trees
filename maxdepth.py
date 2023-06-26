#MAX depth of Binary Tree

def maxDepth(self, root):
        
        def helper(tree):
            if not tree:
                return 0
            maxim = max(helper(tree.left), helper(tree.right)) + 1
            return maxim

        answer = helper(root)
        return answer
