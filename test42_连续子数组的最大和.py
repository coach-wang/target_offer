class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        nCurSum = 0
        nGreatestSum = -float('inf') #负无穷
        for i in array:
            if nCurSum <= 0: #当nCurSum为0或负数的时候，抛弃前面的值
                nCurSum = i
            else:
                nCurSum += i
            if nCurSum > nGreatestSum:
                nGreatestSum = nCurSum
        return nGreatestSum
