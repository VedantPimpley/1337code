# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # edge cases
        if not root:
            return []
        if not (root.left or root.right):
            return [root.val]

        # general case
        '''
        create an output list
        f(1, output)
        about f
            f is a recursive function
            params maxD:int and output:list[int]
            
            base case: node is None, return
            recursive case: 
                if maxD > len(output), append node.val to output
                if root.right, call f(maxD+1, output)
                if root.left, call f(maxD+1, output)

        return output
        '''

        def f(node: Optional[TreeNode], maxD:int, output: list[int]) -> None:
            # base case
            if node is None:
                return
            
            # recursive case
            if maxD > len(output):
                output.append(node.val)
            f(node.right, maxD+1, output)
            f(node.left, maxD+1, output)

        output = []
        f(root, 1, output)
        return output