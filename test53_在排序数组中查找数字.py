#01 数字在排序数组中出现的次数
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        number = 0
        first = self.GetFirstK(data, k)
        last = self.GetLastK(data, k)
        if first > -1 and last > -1:
            number = last - first + 1
        return number
    
    def GetFirstK(self, data, k):
        start, end = 0, len(data) - 1
        while start <= end:
            mid = (start + end) // 2
            if data[mid] == k:
                if (mid > 0 and data[mid - 1] != k) or mid == 0:
                    return mid
                else:
                    end = mid - 1
            elif data[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    
    def GetLastK(self, data, k):
        start, end = 0, len(data) - 1
        while start <= end:
            mid = (start + end) // 2
            if data[mid] == k:
                if (mid < len(data) - 1 and data[mid + 1] != k) or mid == len(data) - 1:
                    return mid
                else:
                    start = mid + 1
            elif data[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        return -1
        
        
