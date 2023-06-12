# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        myNode = None
        nodePointer = None
        while (list1 or list2):
            newNode = ListNode()
            if (list1 and list2):
                if (list1.val > list2.val):
                    newNode.val = list2.val
                    list2 = list2.next
                else:
                    newNode.val = list1.val
                    list1 = list1.next
            elif (list1 or list2):
                if (list1):
                    newNode.val = list1.val
                    list1 = list1.next
                else:
                    newNode.val = list2.val
                    list2 = list2.next
            if (nodePointer == None):
                myNode = newNode
                nodePointer = newNode
            else:
                nodePointer.next = newNode
                nodePointer = nodePointer.next
        return (myNode)
                