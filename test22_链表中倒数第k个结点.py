#单向链表的节点只有从前往后的指针而没有从后往前的指针
#当我们用一个指针遍历链表不能解决问题的时候，可以尝试使用两个指针来遍历链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#1遍历一次
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not isinstance(head, ListNode) or not head:
            return None
        if not isinstance(k, int) or k <= 0:
            return None
        Ahead = head
        Bhead = Ahead
        i = 0
        while i < k-1 and Bhead != None:
            Bhead = Bhead.next
            i += 1
        if Bhead == None:
            return None
        while Bhead.next != None:
            Ahead = Ahead.next
            Bhead = Bhead.next
        return Ahead

#遍历两次
class Solution:
    def FindKthToTail(self, head, k):
        l = []
        while head != None:
            l.append(head)
            head = head.next
        if k > len(1) or k < 1:
            return
        return l[-k]
