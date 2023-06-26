##IN Order Tree Traversal

def inorderTraversal(self, root):

        def helper(tree, answer):
            if not tree:
                return answer
            else:
                helper(tree.left, answer)
                answer.append(tree.val)
                helper(tree.right, answer)
        

        answer = []
        helper(root, answer)
        return answer
