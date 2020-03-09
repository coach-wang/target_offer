class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        pUglyNumbers = [1]
        NumberofUgly = 1
        pMultiply2, pMultiply3, pMultiply5 = 0, 0, 0
        while NumberofUgly < index:
            minVal = min(pUglyNumbers[pMultiply2]*2, pUglyNumbers[pMultiply3]*3, pUglyNumbers[pMultiply5]*5)
            pUglyNumbers.append(minVal)
            while pUglyNumbers[pMultiply2] * 2 <= pUglyNumbers[-1]:
                pMultiply2 += 1
            while pUglyNumbers[pMultiply3] * 3 <= pUglyNumbers[-1]:
                pMultiply3 += 1
            while pUglyNumbers[pMultiply5] * 5 <= pUglyNumbers[-1]:
                pMultiply5 += 1
            NumberofUgly += 1
        return pUglyNumbers[-1]
