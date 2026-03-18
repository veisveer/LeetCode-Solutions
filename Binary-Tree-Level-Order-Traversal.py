1from collections import deque
2
3# Definition for a binary tree node.
4# class TreeNode:
5#     def __init__(self, val=0, left=None, right=None):
6#         self.val = val
7#         self.left = left
8#         self.right = right
9
10class Solution:
11    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
12        if not root:
13            return []
14        
15        output = []
16        
17        queue = deque([root])
18        while queue:
19            size = len(queue)
20            nodes = []
21            for i in range(size):
22                node = queue.popleft()
23                nodes.append(node.val)
24            
25                if node.left:
26                    queue.append(node.left)
27                if node.right:
28                    queue.append(node.right)
29            output.append(nodes)
30        
31        return output