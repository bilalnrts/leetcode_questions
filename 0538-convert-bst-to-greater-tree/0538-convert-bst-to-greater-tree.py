# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (root):
            values = self.BFS(root)
            self.changeTree(root, values)
        return (root)    
        
    def BFS(self, root):
        if (root):
            myQueue = []
            values = []
            myQueue.append(root)
            while (myQueue):
                nodePointer = myQueue.pop(0)
                values.append(nodePointer.val)
                if (nodePointer.left):
                    myQueue.append(nodePointer.left)
                if (nodePointer.right):
                    myQueue.append(nodePointer.right)
            return (values)
    
    def changeTree(self, root, values):
        myQueue = []
        myQueue.append(root)
        while (myQueue):
            nodePointer = myQueue.pop(0)
            nodePointer.val = self.findTotalValue(values, nodePointer.val)
            if (nodePointer.left):
                myQueue.append(nodePointer.left)
            if (nodePointer.right):
                myQueue.append(nodePointer.right)
    
    def findTotalValue(self, values, value):
        total = 0
        for i in values:
            if (i >= value):
                total += i
        return (total)