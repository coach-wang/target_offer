class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#方法1
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None or pHead.next == None or pHead.next.next == None:
            return None
        #确定链表中是否包含环
        meetingNode = self.MeetingNode(pHead)
        if meetingNode == None:
            return pHead
        
        #统计环内节点数
        nodesInloop = 1
        pNode1 = meetingNode
        while pNode1.next != meetingNode:
            pNode1 = pNode1.next
            nodesInloop += 1
            
        #寻找环的入口
        #先让pNode2移动nodesInloop次，然后pNode1和pNode2同时移动，两指针相遇使，即是环的入口节点
        pNode2 = pHead
        for i in range(nodesInloop):
            pNode2 = pNode2.next
        pNode1 = pHead
        while pNode1 != pNode2:
            pNode1 = pNode1.next
            pNode2 = pNode2.next
        return pNode1
    
    def MeetingNode(self, pHead):
        pSlow = pHead
        pFast = pSlow
        meet = False
        while pFast.next and pFast.next.next and meet != True:
            pSlow = pSlow.next
            pFast = pFast.next.next
            if pFast == pSlow:
                meet = True
        if pFast == None or pFast.next == None:
            return None
        return pFast

#方法2 参考https://www.cnblogs.com/fankongkong/p/7007869.html
class Solution:
    def EntryNodeOfLoop(self, pHead):
        pNode1 = meetingNode
        pNode2 = pHead
        while pNode1 != pNode2:
            pNode1 = pNode1.next
            pNode2 = pNode2.next
        return pNode1

#方法3 用append
class Solution:
    def EntryNodeOfLoop(self, pHead):
        templist = []
        p = pHead
        while p:
            if p in templist:
                return p
            else:
                templist.append(p)
            p = p.next
