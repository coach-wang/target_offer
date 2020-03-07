'''
长度为1~3的线段，不切分的话是乘积最大的
'''
#1动态规划法
class Solution:
    def cutRope(self, number):
        # write code here
        if number == 2:
            return 1
        elif number == 3:
            return 2
        products = [0]*(number+1)
        products[1] = 1
        products[2] = 2
        products[3] = 3
        #长度为3的线段，不切分的话成绩最大，所以这里3个数字是不切分时的最大长度
        
        for n in range(4, number+1):
            max = 0
            for i in range(1, int(n/2)+1):
                product = products[i] * products[n-i]
                if max < product:
                    max = product
            products[n] = max
        return products[number]

#2贪婪算法
class Solution:
    def cutRope(self, number):
        # write code here
        if number == 2:
            return 1
        elif number == 3:
            return 2
        timesOf3 = number//3
        if number - timesOf3*3 == 1:
            timesOf3 -= 1
            
        timesOf2 = (number - timesOf3 * 3)/2
        
        return int(pow(3, timesOf3) * pow(2, timesOf2))    
