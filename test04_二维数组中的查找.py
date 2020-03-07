class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array[0]) == 0 or len(array) == 0:
            print('empty list')
            return False
        m = len(array)
        n = len(array[0])
        rows, columns = 0, n-1
        while rows < m and columns >= 0:
            if target == array[rows][columns]:
                return True
            elif target < array[rows][columns]:
                columns -= 1
            else:
                rows += 1
        return False
