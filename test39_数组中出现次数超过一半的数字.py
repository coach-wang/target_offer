class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not isinstance(numbers, list) or not numbers:
            return 0
        result = [numbers[0], 1]
        for i in numbers[1:]:
            if i == result[0]: #如果该数字与记录的数字相同，则次数加1
                result[1] += 1
            else:
                result[1] -= 1
                if result[1] == 0:
                    result[0] = i
                    result[1] = 1
        if self.CheckMoreThanHalf(numbers, result[0]):
            return result[0]
        else:
            return 0
    
    def CheckMoreThanHalf(self, numbers, number):
        times = 0
        for i in numbers:
            if number == i:
                times += 1
        if times > (len(numbers)>>1):
            return True
        else:
            return False
