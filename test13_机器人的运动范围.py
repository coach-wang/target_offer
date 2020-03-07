class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0 or rows <= 0 or cols <=0:
            return 0
        visited = [[0 for i in range(cols)]for j in range(rows)]
        count = self.movingCountCore(threshold, rows, cols, 0, 0, visited)
        return count
    
    def movingCountCore(self, threshold, rows, cols, i, j, visited):
        count = 0
        if self.check(threshold, rows, cols, i, j, visited):
            visited[i][j] = True
            count = 1 +self.movingCountCore(threshold, rows, cols, i-1, j, visited) + self.movingCountCore(threshold, rows, cols, i+1, j, visited) + self.movingCountCore(threshold, rows, cols, i, j-1, visited) + self.movingCountCore(threshold, rows, cols, i, j+1, visited)
        return count
    
    def check(self, threshold, rows, cols, i, j, visited):
        if 0<=i<rows and 0<=j<cols and self.getDigitSum(i, j) <= threshold and not visited[i][j]:
            return True
        return False
    
    def getDigitSum(self, i, j):
        a = 0
        for index in str(i):
            a += int(index)
        for index in str(j):
            a += int(index)
        return a
