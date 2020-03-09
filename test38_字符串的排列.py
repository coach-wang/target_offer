      #intertools里有permutation函数可用
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        self.vis = [0 for i in range(len(ss))]
        self.ans = []
        self.temp = ""
        self.DFS(0, ss)
        return sorted([i for i in set(self.ans)])  #使用set函数排除重复，sort排序用
    
    def DFS(self, sum, ss):
        if sum == len(ss):
            self.ans.append(self.temp)
            return
        for idx in range(len(ss)):
            if self.vis[idx] == 0:
                self.vis[idx] = 1
                self.temp += ss[idx]
                self.DFS(sum + 1, ss)
                self.temp = self.temp[:-1]
                self.vis[idx] = 0
                
