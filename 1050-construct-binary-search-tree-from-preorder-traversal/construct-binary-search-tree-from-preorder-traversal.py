# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        N = len(preorder)
        if N == 1:
            return TreeNode(val=preorder[0])
        
        val_root = preorder.pop(0)
        j = N
        for i, e in enumerate(preorder):
            if val_root < e:
                j = i
                break
        
        return TreeNode(val = val_root, left=self.bstFromPreorder(preorder[:j]), right = self.bstFromPreorder(preorder[j:]))
        
            
            
            