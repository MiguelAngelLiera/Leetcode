# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from copy import deepcopy
class Solution:
    """
    [1,2,4,8], [1,2,4,9]
    
    [5,4,8,11,null,17,4,7,1,null,null,5,3]: List[nodes]
    [5,9,13,20, ..., ]: List[int]
    """
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        if not root.left and not root.right:
            return None if root.val < limit else root
        tmp, sum_ = self.aux(root, limit, 0)
        if tmp is not None and sum_ < limit:
            return None
        return tmp
        
    def aux(self, node: Optional[TreeNode], limit: int, sum_: int) -> Tuple[TreeNode, int]:
        if not node:
            return None, -float(inf)
        
        sum_ += node.val
        if not node.left and not node.right:
            return node, node.val
                
        _, left_ = self.aux(node.left, limit, sum_)
        _, right_ = self.aux(node.right, limit, sum_)
        
        if sum_ + left_ < limit:
            node.left = None
            
        if sum_ + right_ < limit:
            node.right = None
            
        return node, node.val + max(right_, left_)
            