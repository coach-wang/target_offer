#01 求斐波那契数列的第n项
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            One, Two, fibN = 0, 1, 0
            for i in range(2,n+1):
                fibN = One + Two
                One, Two = Two,fibN
            return fibN

#02 青蛙跳台阶问题
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            One, Two ,fibN = 1, 2, 0
            for i in range(3, number+1):
                fibN = One + Two
                One, Two = Two, fibN
            return fibN
#03 变态跳台阶
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 0:
            return 0
        elif number == 1:
            return 1
        else:
            One, way = 1, 0
            for i in range(2, number+1):
                way = One*2
                One = way
            return way
#04 矩形覆盖
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        else:
            One, Two, fibN = 1, 2, 0
            for i in range(3, number+1):
                fibN = One + Two
                One, Two = Two, fibN
            return fibN
