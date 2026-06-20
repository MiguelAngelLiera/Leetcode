# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        p = []
        self.iterate_tree(root, targetSum, p)
        return len(p)

    def iterate_tree(self, root: Optional[TreeNode], targetSum: int, paths: List[List[int]]) -> List[List[int]]:
        if not root:
            return []
        paths += self.backtrack(root, targetSum)
        self.iterate_tree(root.left, targetSum, paths)
        self.iterate_tree(root.right, targetSum, paths)
        
    def backtrack(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        if targetSum == root.val:
            paths = [[root.val]]
            paths += self.backtrack(root.left, 0)
            paths += self.backtrack(root.right, 0)
            return paths
        paths = []
        for child in [root.left, root.right]:
            paths += [[root.val] + path for path in self.backtrack(child, targetSum - root.val)]
        return paths