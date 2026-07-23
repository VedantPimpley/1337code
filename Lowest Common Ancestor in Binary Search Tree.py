# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        requires:
            tree is non-empty
            p and q exist in the tree
        ensures:
            q is in subtree of p -> p is lca
            p is in subtree of q -> q is lca
        algo:
            find p and q at the same time
            when the cur nd differs, return prev node "lca"

            lca = root

            ca1, ca2 = root, root
            p_found, q_found = False, False
            while not p_found and not q_found:
                
                if ca1 == p:
                    p_found = True
                if not p_found:
                    ca1 = ca1.left if p.val < ca1.val else ca1.right
                
                if ca2 == q:
                    q_found = True
                if not q_found:
                    ca2 = ca2.left if q.val < ca2.val else ca2.right
                
                if ca1 == ca2:
                    lca = ca1
                else:
                    break

            return lca
        '''

        # general case
        lca = None
        ca1, ca2 = root, root
        while ca1 == ca2:
            lca = ca1
            
            if ca1 == p:
                pass
            else:
                ca1 = ca1.left if p.val < ca1.val else ca1.right
            
            if ca2 == q:
                pass    
            else:
                ca2 = ca2.left if q.val < ca2.val else ca2.right
            
        return lca