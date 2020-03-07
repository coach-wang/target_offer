class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pReversedHead = None
        pNode = pHead
        pPrev = None #pnode之前的指针
        if pNode == None:
            return None
        elif pHead.next == None:
            return pHead
        while pNode:
            pNext = pNode.next
            if not pNext: 
                pReversedHead = pNode
            pNode.next = pPrev #翻转指针指向
            pPrev = pNode
            pNode = pNext
        return pReversedHead
