#PRE order Traversal N-Ary Tree

def preorder(self, root):
        
        answer = []

        def helper(tree):
            if tree:
                answer.append(tree.val)
                for item in tree.children:
                    helper(item)
            
        helper(root)
        return answer