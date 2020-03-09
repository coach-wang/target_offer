# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        self.CloneNodes(pHead)
        self.ConnectSiblingNodes(pHead)
        return self.ReconnectNodes(pHead)
    
    def CloneNodes(self, pHead):
        #根据原始链表的每个节点N创建对应的N'，把N'放在N的后面
        p = pHead
        while p:
            temp = RandomListNode(p.label)
            temp.next = p.next
            p.next = temp
            p = temp.next
    
    def ConnectSiblingNodes(self, pHead):
        p = pHead
        while p:
            if p.random:
                p_clone = p.next
                p_clone.random = p.random.next
            p = p.next.next
    
    def ReconnectNodes(self, pHead):
        p1 = pHead
        p2 = pHead.next
        Clone_Node_Head = pHead.next
        while p1 and p2:
            p1.next = p2.next
            if not p2.next:
                break
            p2.next = p2.next.next
            p1 = p1.next
            p2 = p2.next
        return Clone_Node_Head
    
