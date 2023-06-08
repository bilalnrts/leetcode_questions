# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sumOfValues = 0
        if (root == None):
            return

        def traverse(node):
            nonlocal sumOfValues
            
            if (node.right):
                traverse(node.right)
            
            #operations
            temp = node.val
            node.val += sumOfValues
            sumOfValues += temp
            
            if (node.left):
                traverse(node.left)
        
        traverse(root)
        return (root)