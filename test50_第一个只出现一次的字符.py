#01 字符串中第一个只出现一次的字符
'''
如果需要判断多个字符是不是在某个字符串里出现过或者统计多个字符在某个字符串中出现的次数，
那我们可以考虑基于数组创建一个简单的哈希表，这样可以用很小的空间消耗换来时间效率的提升
'''
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        Hash_Map = {}
        for i in range(len(s)):
            Hash_Map[s[i]] = Hash_Map.get(s[i], 0) + 1  #get函数，dict.get(key, default)
                                                        #其中key为字典中查找的键，当key不存在时
                                                        #返回default值。
        for i in range(len(s)):
            if Hash_Map[s[i]] == 1:
                return i
        return -1

#02 字符流中第一个不重复的字符
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.Hash_Map = {}
        
    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.Hash_Map[i] == 1:
                return i
        return '#'
    
    def Insert(self, char):
        # write code here
        self.s += char
        self.Hash_Map[char] = self.Hash_Map.get(char, 0) + 1
