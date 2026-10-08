"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ogNodes = {}
        cNodes = {}
        nodeRel = {}
        h1 = head
        while h1:
            newNode = Node(h1.val)
            nodeRel[h1] = newNode
            h1 = h1.next
        
        curr = head
        while curr:
            temp = nodeRel.get(curr)
            temp.next = nodeRel.get(curr.next)
            temp.random = nodeRel.get(curr.random)
            curr = curr.next
        return nodeRel.get(head)
        
            
        