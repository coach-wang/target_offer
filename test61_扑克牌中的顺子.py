class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers or len(numbers) != 5:
            return False
        numbers.sort()
        
        numberOfZeros = 0
        for i in numbers:
            if i == 0:
                numberOfZeros += 1
        
        numberOfGap = 0
        small = numberOfZeros
        while small < len(numbers) - 1:
            if numbers[small] == numbers[small + 1]:
                return False
            numberOfGap += numbers[small + 1] - numbers[small] - 1
            small += 1
        return False if numberOfGap > numberOfZeros else True
