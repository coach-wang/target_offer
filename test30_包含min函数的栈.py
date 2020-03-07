class Solution:
    def __init__(self):
        self.m_data = [] #数据栈
        self.m_min = [] #辅助栈
        
    def push(self, node):
        # write code here
        self.m_data.append(node)
        
        if len(self.m_min) == 0 or node < self.m_min[-1]:
            self.m_min.append(node)
        else:
            self.m_min.append(self.m_min[-1])
            
    def pop(self):
        # write code here
        if len(self.m_data):
            self.m_data.pop()  #pop函数默认移除列表的最后一位
            self.m_min.pop()
        else:
            return
        
    def top(self):
        # write code here
        if len(self.m_data):
            return self.m_data[-1]
        else:
            return
        
    def min(self):
        # write code here
        if len(self.m_data):
            return self.m_min[-1]
        else:
            return
