# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if not root:
            return []
        ans = []
        q = deque()
        q.append(root)
        while q:
            level = []
            n = len(q)
            for i in range (n) :
                pn = q.popleft()
                level.append(pn.val)
                if pn.left :
                    q.append(pn.left)
                if pn.right :
                    q.append(pn.right)
            ans.append(sum(level)/len(level))
        return ans
        