#POST Order n-ary tree

def postorder(self, root):
       
        answer = []
        def helper(tree):
            if tree:
                for item in tree.children:
                    helper(item)
                answer.append(tree.val)

        helper(root)
        return answer