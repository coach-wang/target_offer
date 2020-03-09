#1 翻转单词顺序
class Solution:
    def ReverseSentence(self, s):
        # write code here
        #使用python中的split函数，分割字符串
        #s1 = s.split(' ')
        #return ' '.join(s1[::-1])
        
        self.s = list(s)
        self.Reverse(0, len(self.s)-1)
        pBegin, pEnd = 0, 0
        while pBegin < len(self.s):
            if self.s[pBegin] == ' ':
                pBegin += 1
                pEnd += 1
            elif pEnd == len(self.s) or self.s[pEnd] == ' ':
                self.Reverse(pBegin, pEnd - 1)
                pBegin = pEnd + 1
                pEnd += 1
            else:
                pEnd += 1
        return ''.join(self.s)
    
    def Reverse(self, pBegin, pEnd):
        while pBegin < pEnd:
            self.s[pBegin], self.s[pEnd] = self.s[pEnd], self.s[pBegin]
            pBegin += 1
            pEnd -= 1

#2 左旋转字符串
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ''
        if n < 0 or n > len(s):
            return ''
        if n == len(s):
            return ''.join(s)
        #1简便方法
        #return s[n:] + s[:n]
        #法2
        self.s = list(s)
        self.Reverse(0, len(s)-1)
        self.Reverse(0, len(s)-n-1)
        self.Reverse(len(s)-n, len(s)-1)
        return ''.join(self.s)
    
    def Reverse(self, pBegin, pEnd):
        while pBegin < pEnd:
            self.s[pBegin], self.s[pEnd] = self.s[pEnd], self.s[pBegin]
            pBegin += 1
            pEnd -= 1
