class Solution:
    #将数组不断一分为二，直到数组中只有两个元素，统计逆序对个数，然后将相邻两个子数组进行合并
    #逆序对的总数 = 左边数组中逆序对的数量+右边数组逆序对的数量+左右结合成新的顺序数组时出现逆序对数量
    #时间复杂度O(nlogn),构建了一个长度为n的辅助数组
    def InversePairs(self, data):
        # write code here
        num, new_list = self.mergeSort(data)  #New_list是排序后的数列
        return num%1000000007
    
    def mergeSort(self, data):
        InversePairsNum = 0 #逆序对个数
        if len(data) <= 1:
            return 0, data
        else:
            mid = len(data) // 2  #一分为二计算，直到分到数组只有两个元素
            num_left, left_list = self.mergeSort(data[:mid]) #左部分
            num_right, right_list = self.mergeSort(data[mid:]) #右部分
            num_merge, new_list = self.merge(left_list, right_list) #左右两部分合并后新增的逆序
            InversePairsNum = num_left + num_right + num_merge
            return InversePairsNum, new_list
    
    def merge(self, left, right):
        #计算合并后发现的逆序对个数
        InversePairNum = 0
        result = []  #保存合并后的结果
        i = j = 0 #两个指针
        while(i<len(left) and j<len(right)):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                InversePairNum += (len(left)-i)
        result = result + left[i:] + right[j:] #剩余的元素添加到末尾
        return InversePairNum, result
            
