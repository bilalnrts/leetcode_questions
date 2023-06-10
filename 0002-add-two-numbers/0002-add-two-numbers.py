# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = int(self.listToStr(l1)[::-1])
        l2 = int(self.listToStr(l2)[::-1])
        sumVal = l1 + l2
        return (self.createResult(sumVal))
        
    def listToStr(self, node):
        mystr = ""
        while (node):
            mystr += str(node.val)
            node = node.next
        return (mystr)
    
    def createResult(self, num):
        if (num == 0):
            return (ListNode(0)) 
        firstNode = None
        nodePointer = None
        while (num):
            newNode = ListNode()
            newNode.val = num % 10
            newNode.next = None
            if nodePointer == None:
                firstNode = newNode
                nodePointer = newNode
            else:
                nodePointer.next = newNode
                nodePointer = newNode
            num //= 10
        return (firstNode)
        
        