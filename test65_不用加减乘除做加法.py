#1 位运算，超时了 参考https://blog.csdn.net/lrs1353281004/article/details/87192205
class Solution:
    def Add(self, num1, num2):
        while num2 != 0:
            carry = (num1 & num2) << 1  #进位
            num1 = (num1 ^ num2)  #异或
            num2 = carry 
        return num1 if num1<=0x7FFFFFFF else num1 |(~0x100000000+1) #考虑边界条件

#2 使用sum函数
class Solution:
    def Add(self, num1, num2):
        return sum([num1, num2])
