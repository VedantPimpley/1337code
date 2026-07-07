# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        requires:
            len(preorder) == len(inorder)
            len(preorder) >= 1
            all values are unique
        ensures:
            number of nodes in returned tree == len(preorder) == len(inorder)
        algo:
            # inorder: LNR
            # preorder: NLR
            # both are a kind of DFS traversal
            [1]: [2], [3]
            [3]: [4]
            
            1 - 2, 3
            2 - -, -
            3 - 4, -

            # establish parent child relationships and build tree as you go along


            --------

            App. Start with preorder/inorder, see what info is missing, look that info up in inorder/postorder, combine this info to construct a par:child dict.
        '''
        
        n = len(preorder)
        root = TreeNode(preorder[0])

        # edge case
        if n == 1:
            return root

        # general case
        seen_in_inorder = set([x for x in inorder])
        for i in preorder[1:]:
