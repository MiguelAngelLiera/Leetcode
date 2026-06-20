# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[]]
        queue = deque()
        queue.append(root)
        level = 1

        while queue:
            if level == 0:
                res.append([])
                level = len(queue)
            curr = queue.popleft()
            level -= 1
            res[-1].append(curr.val)

            for child in [curr.left, curr.right]:
                if child:
                    queue.append(child)

            
                    
        
        return res
        