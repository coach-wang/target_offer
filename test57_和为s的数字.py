#1 和为s的两个数字
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        left, right = 0, len(array) - 1
        while left <= right:
            temp = array[left] + array[right]
            if temp == tsum:
                return [array[left], array[right]]
            elif temp < tsum:
                left += 1
            else:
                right -= 1
        return []

#2 和为s的连续正数序列
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        small, big = 1, 2
        mid = (1 + tsum) >> 1
        curSum = small + big
        result = []
        while small < mid:
            if curSum == tsum:
                result.append(list(range(small, big + 1)))
            while curSum > tsum and small < mid:
                curSum -= small
                small += 1
                if curSum == tsum:
                    result.append(list(range(small, big + 1)))
            big += 1
            curSum += big
        return result
