# T.C = O(n) S.C = O(h)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    #result = []
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self.dfs(root,0)
        return self.result

    def dfs(self,root,level):
        if(root is None):
            return
        
        if(len(self.result) == level):
            self.result.append(root.val)

        self.dfs(root.right,level+1)
        self.dfs(root.left,level+1)
        
        