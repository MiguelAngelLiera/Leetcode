# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = self.backtrack(root)
        strings = []
        for path in paths:
            string = ""
            for e in path:
                string += f"{e}->"
            string = string[:-2]
            strings.append(string)
        return strings

    def backtrack(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]
        paths = []
        for child in [root.left, root.right]:
            child_paths = self.backtrack(child)
            paths += [[root.val] + path for path in child_paths]
        
        return paths
        


        