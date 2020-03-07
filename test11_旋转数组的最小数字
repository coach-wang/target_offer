'''
使用二分法要注意数字重复的情况
'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not isinstance(rotateArray, list) or not rotateArray:
            return 0
        start, end = 0, len(rotateArray)-1
        mid = start
        while rotateArray[start] >= rotateArray[end]:
            if end - start == 1:
                return rotateArray[end]
            mid = int((start+end)/2)
            if rotateArray[start]==rotateArray[mid]==rotateArray[end]:
                mid = MinInOrder(rotateArray, start, end)
                return rotateArray[mid]
            if rotateArray[mid]>=rotateArray[start]:
                start = mid
            elif rotateArray[mid]<=rotateArray[end]:
                end = mid
    
    def MinInOrder(Array, start, end):
        val, min = Array[start], start
        for i in range(start, end+1):
            if Array[i]<val:
                val = Array[i]
                min = i
        return min
