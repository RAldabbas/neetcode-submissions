# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [root]
        mp = {None: 0}
        while stack:
            curr = stack.pop()
            if curr in mp:
                leftH = mp[curr.left]
                rightH = mp[curr.right]
                mp[curr] = 1 + max(leftH, rightH)
                if abs(leftH - rightH) > 1:
                    return False

            else:
                stack.append(curr)
                mp[curr] = 0
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
        return True
            
            