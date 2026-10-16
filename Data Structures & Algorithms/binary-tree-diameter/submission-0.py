# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root)]
        mp = {None: 0}
        res = 0

        while stack:
            curr = stack.pop()
            if curr in mp:
                leftH = mp[curr.left] if curr.left else 0
                rightH = mp[curr.right] if curr.right else 0
                mp[curr] = 1 + max(leftH, rightH)
                res = max(res, leftH + rightH)
            else:
                stack.append(curr)
                mp[curr] = 0
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                
            
        return res