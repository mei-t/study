from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 5:17
# N is the number of nodes.
# TC: O(N)
# SC: O(N) (balanced treeの時、SCの最大値はleafの数になる。この時N/2となるためSCはO(N)。)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        nodes = [root] if root else None
        res = 0
        while nodes:
            res += 1
            nextNodes = list()
            for node in nodes:
                if node.left: nextNodes.append(node.left) 
                if node.right: nextNodes.append(node.right)
            nodes = nextNodes
        
        return res