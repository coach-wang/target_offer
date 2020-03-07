class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1
        
        pAnode, pBnode = pHead1, pHead2
        #头指针，指向较小的值
        if pAnode.val < pBnode.val:
            pHead = pAnode
            pAnode = pAnode.next
        else:
            pHead = pBnode
            pBnode = pBnode.next
        
        p1 = pHead #p1用于移动
        while pAnode and pBnode:
            if pAnode.val < pBnode.val:
                p1.next = pAnode 
                pAnode = pAnode.next
            else:
                p1.next = pBnode
                pBnode = pBnode.next
            p1 = p1.next
        
        #当其中一个指针走到最后时，补上另一个指针。
        while pBnode and (pAnode == None):
            p1.next = pBnode
            pBnode = pBnode.next
            p1 = p1.next
        while pAnode and (pBnode == None):
            p1.next = pAnode
            pAnode = pAnode.next
            p1 = p1.next
        
        return pHead
