# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if not q or not p:
            return False
        queue1 = deque([p])
        queue2 = deque([q])

        while queue1 or queue2:
            curr1 = queue1.popleft()
            curr2 = queue2.popleft()
            if curr1 is None and curr2 is None:
                continue
            if curr1 is None or curr2 is None:
                return False
            if curr1.val != curr2.val:
                return False

            if curr1.left or curr2.left:
                queue1.append(curr1.left)
                queue2.append(curr2.left)
            if curr1.right or curr2.right:
                queue1.append(curr1.right)
                queue2.append(curr2.right)
        return not queue1 and not queue2