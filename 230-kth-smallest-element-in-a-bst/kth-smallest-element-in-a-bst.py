# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order_list = self.in_order(root)
        return in_order_list[k-1]
    
    def in_order(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.in_order(root.left) + [root.val] + self.in_order(root.right)


        
        