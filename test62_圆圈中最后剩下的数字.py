#class Node:
    #def __init__(self, data, next = None):
        #self.data = data
        #self.next = next

#方法1 链表法，时间复杂度O（mn），空间复杂度O（n）
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        head = Node(0) #创建一个环形链表
        p = head
        for i in range(1, n):
            temp = Node(i)
            p.next = temp
            p = temp
        p.next = head
        
        p = head
        while n > 1:
            for i in range(m-1):
                p = p.next
            temp = p.next #弹出该元素
            p.data, p.next = temp.data, temp.next 
            n -= 1
        return p.data

#方法2 分析数字特征
class Solution:
    def LastRemaining_Solution(self, n, m):
          if m < 1 or n < 1:
            return -1
        res = range(n)
        i = 0  
        while len(res)>1:
            i = (m+i-1)%len(res) #每次弹出的数字，也是下一次开始的起点
            res.pop(i)
        return res[0]
        
