'''

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        pNode = pHead.next
        if pNode.val != pHead.val:
            pHead.next = self.deleteDuplication(pHead.next)
        else:
            while pNode.val == pHead.val and pNode.next:
                pNode = pNode.next
            if pNode.val != pHead.val:
                pHead = self.deleteDuplication(pNode)
            else:
                return None
        return pHead
