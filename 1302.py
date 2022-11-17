# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        next_lvl = [root]
        prev_lvl = []

        while next_lvl:
            prev_lvl = next_lvl
            next_lvl = []

            for node in prev_lvl:
                if node.left: next_lvl.append(node.left)
                if node.right: next_lvl.append(node.right)

        return sum([node.val for node in prev_lvl])
