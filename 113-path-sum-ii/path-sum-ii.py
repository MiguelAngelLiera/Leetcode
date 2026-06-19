# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return self.backtrack(root, targetSum)
    
    def backtrack(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            if root.val == targetSum:
                return [[root.val]]
        paths = []
        for child in [root.left, root.right]:
            paths += [[root.val] + path for path in self.backtrack(child, targetSum - root.val)]
        return paths
        