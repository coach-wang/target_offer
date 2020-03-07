class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not isinstance(pushV, list) or not isinstance(popV, list):
            return False
        if len(pushV) != len(popV):
            return False
        stack = [] #辅助栈
        j = 0 #用于控制popV的index
        for i in pushV:
            stack.append(i)
            while stack and stack[-1] == popV[j]:
                stack.pop()
                j += 1
        if stack:
            #若栈中仍有元素
            return False
        else:
            return True
        
