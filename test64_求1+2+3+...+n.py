class Solution:
    def __init__(self):
        self.sum = 0
    def Sum_Solution(self, n):#用了闭包的概念
        # write code here
        def qiusum(n):
            self.sum += n
            n -= 1
            return n >0 and self.Sum_Solution(n) #当n为0或负数时，自动忽略之后的递归
        qiusum(n)
        return self.sum
