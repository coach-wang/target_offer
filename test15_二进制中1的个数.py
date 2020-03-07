#1 左移法
#除法的效率比移位运算低很多
class Solution:
    def NumberOf1(self, n):
        count, flag = 0, 1
        if n < 0:
            n = n & 0xffffffff
            #n *= -1
            #count = 1 这种方法遇到-214783648时取正数时会溢出，不可取
        while flag and flag <=n:
            if n & flag:
                count += 1
            flag = flag << 1
        return count
        
#减1做与运算
#把一个整数减去1再和原来的整数做位与运算，得到的结果相当于把整数的二进制表示中最右边的1变成0。很多二进制问题都可以用这种方法
class Solution:
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n-1) & n
        return count
    
