#解法1 需要修改输入数组，时间复杂度为o(n)
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or len(tinput)<k or k<=0:
            return []
        pivot = self.Partition(tinput, 0, len(tinput)-1)
        while pivot != (k-1):
            if pivot>k:
                pivot = self.Partition(tinput, 0, pivot-1)
            else:
                pivot = self.Partition(tinput, pivot+1, len(tinput)-1)
        return sorted(tinput[:k])
    
    def Partition(self, numbers, low, high):
        key = numbers[low] #选一个数字key，比key小的排到low左边，比key大的排到low的右边
        while low < high:
            while low < high and numbers[high] >= key:
                high -= 1
            numbers[low], numbers[high] = numbers[high], numbers[low]
            while low < high and numbers[low] <= key:
                low += 1
            numbers[low], numbers[high] = numbers[high], numbers[low]
        return low
        
#解法二 时间复杂度为O(nlogk),不需要修改数组，适用于海量数据
Class Solution2:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or len(tinput)<k or k<=0:
            return []
        vec = [x for x in tinput[:k]]    #这里更好可以用最大堆作为容器，时间复杂度更低，但我不会
        MaxIndex = self.Find_Max(vec)
        for i in tinput[k:]:
            if i < vec[MaxIndex]:
                vec[MaxIndex] = i
                MaxIndex = self.Find_Max(vec)
        return sorted(vec)
        
    def Find_Max(self, lis):
        return lis.index(max(lis))
