# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (root):
            myRoot = TreeNode(root.val)
            self.mySolution(root, myRoot)
            return myRoot
        
    def mySolution(self, root, myroot):
        if (root.left != None):
            myroot.right = TreeNode(root.left.val)
            self.mySolution(root.left, myroot.right)
        if (root.right != None):
            myroot.left = TreeNode(root.right.val)
            self.mySolution(root.right, myroot.left)
        if (root.right == None and root.left == None):
            return

            
            