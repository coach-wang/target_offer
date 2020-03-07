class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not isinstance(matrix, list):
            return
        m, n = len(matrix), len(matrix[0])
        res = []
        #if m == 1 and n == 1:
            #res = [matrix[0][0]]
            #return res
        for i in range((min(m,n)+1)//2):
            endX, endY = n - 1 - i, m - 1 -i
            #1.从左到右打印一行
            for a in range(i, endX + 1):
                res.append(matrix[i][a])
            #2.从上到下打印一列  前提：终止行号大于起始行号
            if endY > i:
                for b in range(i + 1, endY + 1):
                    res.append(matrix[b][endX])
            #3.从右到左打印一行  前提：圈内至少有两行两列，即要求终止行号大于起始行号且终止列号大于起始列号
            if endX > i and endY > i:
                for c in range(endX - 1, i - 1, -1):
                    res.append(matrix[endY][c])
            #4.从下到上打印一列
            if endX > i and endY > i + 1:
                for d in range(endY - 1, i, -1):
                    res.append(matrix[d][i])
        return res
