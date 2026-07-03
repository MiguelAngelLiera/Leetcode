# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if (root.left is None and root.right is None):
            return [root.val]
        root_b = [root.val]
        left_b = []
        if root.left:
            curr = root.left
            if (curr.left or curr.right):
                left_b.append(curr.val)
                while curr.left or curr.right:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr = curr.right
                    if (curr.left or curr.right): 
                        left_b.append(curr.val)
                        
        right_b = []
        if root.right:
            curr = root.right
            if (curr.left or curr.right):
                right_b.append(curr.val)
                while curr.left or curr.right:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr = curr.left
                    if (curr.left or curr.right): 
                        right_b.append(curr.val)
                        
        right_b = right_b[::-1]
        leafs_b = self.bfs_only_leafs(root)
        
        #print(leafs_b)
        
        return root_b + left_b + leafs_b + right_b
    
    def dfs_only_leafs(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        queue = []
        queue.append(root)
        
        while queue:
            
            curr = queue.pop(0)
            
            if not curr.left and not curr.right:
                visited.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        return visited
    
    def bfs_only_leafs(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        
        leafs = []
        for child in [root.left, root.right]:
            leafs += self.bfs_only_leafs(child)
            
        return leafs
            
        
        
        
        
        
        
        
        
        
        