# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        nLength1 = self.GetLength(pHead1)
        nLength2 = self.GetLength(pHead2)
        nLengthDif = abs(nLength1 - nLength2)
        
        LongListNode, ShortListNode = pHead1, pHead2
        if nLength1 < nLength2:
            LongListNode, ShortListNode = pHead2, pHead1
        for i in range(nLengthDif):
            LongListNode = LongListNode.next
        while LongListNode and ShortListNode and LongListNode != ShortListNode:
            LongListNode = LongListNode.next
            ShortListNode = ShortListNode.next
        return LongListNode
    
    def GetLength(self, pHead):
        i = 0
        p = pHead
        while p:
            i+=1
            p = p.next
        return i
