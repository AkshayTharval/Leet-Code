# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s, t):
        tree1 = self.preorder(s)
        tree2 = self.preorder(t)
        return tree2 in tree1 
    
    def preorder(self, node): 
        if node is None:
            return 'null'
        return ' '+ str(node.val) + " " + self.preorder(node.left) + " " + self.preorder(node.right)
        