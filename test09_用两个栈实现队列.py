'''
当stack2不为空时，在stack2中的栈顶元素是最先进入队列的元素，可以弹出。
当stack2为空时，我们把stack1中的元素逐个弹出并压入stack2
'''
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, node):
        # write code here
        if not node:
            return
        self.stack1.append(node)
        
    def pop(self):
        # return xx
        if not self.stack1 and not self.stack2:
            return
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
