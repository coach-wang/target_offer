class Solution:
    def reOrderArray(self, array):
        # write code here
        if not isinstance(array, list) or not array:
            return array
        count = 0
        for i in range(0, len(array)):
            for j in range(len(array)-1, i, -1):
                if array[j-1]%2 == 0 and array[j]%2 == 1:
                    temp = array[j-1]
                    array[j-1] = array[j]
                    array[j] = temp
        return array
    
