# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxSoFar = 0
        currDepth = 0
        if not root:
            return 0
        stack = [(root, 0)]
        
        while stack:
            curr, currDepth = stack.pop()
            currDepth += 1
            maxSoFar = max(currDepth, maxSoFar)
            
            if curr.left:
                stack.append((curr.left, currDepth))
            if curr.right:
                stack.append((curr.right, currDepth))
        return maxSoFar
