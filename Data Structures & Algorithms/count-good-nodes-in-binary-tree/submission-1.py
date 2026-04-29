# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        ans = 0

        def dfs(node, maxi):
            nonlocal ans
            if not node: return
            elif node.val>=maxi:
                ans+=1
            
            dfs(node.left, max(maxi,node.val))
            dfs(node.right, max(maxi,node.val))

        dfs(root, float('-inf'))
        return ans

