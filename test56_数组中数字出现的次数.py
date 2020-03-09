#01 数组中只出现一次的两个数字
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array or len(array)<2:
            return
        resultExclusiveOR = 0
        for i in array:
            resultExclusiveOR ^= i #^异或
        if resultExclusiveOR == 0:
            return
        indexOf1 = self.FindFirstBitIs1(resultExclusiveOR)
        
        num1, num2 = 0, 0
        for i in array:
            if self.IsBit1(i, indexOf1): #第n位为1的那一组
                num1 ^= i
            else:#第n位为0的那一组
                num2 ^= i
        return sorted([num1, num2])
    
    def FindFirstBitIs1(self, num):
        indexBit = 0#要找的第n位
        while num & 1 == 0:#与
            num = num >> 1
            indexBit += 1
        return indexBit
    
    def IsBit1(self, num, indexBit):
        num = num >> indexBit
        return num & 1
