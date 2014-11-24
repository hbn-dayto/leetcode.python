# *********************************************
# Source : https://oj.leetcode.com/problems/path-sum/
# Author : wizcabbit
# Date   : 2014-11-20

# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# *********************************************

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
      if root is None:
        return False
      else:
        # Only leaf could return true
        if sum == root.val and root.left is None and root.right is None:
          return True
        else:
          return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
