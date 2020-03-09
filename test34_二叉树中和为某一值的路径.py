# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        path = []
        Res = []
        Res = self.Find_Path(root, expectNumber, path, Res)
        return Res
    
    def Find_Path(self, root, expectNumber, path, Res):
        path.append(root)
        currentSum = 0
        res = []
        for j in path:
            currentSum += j.val  
        #如果是叶节点，且路径上的节点值之和等于输入的值，则打印
        isLeaf = (root.left == None and root.right == None)
        if currentSum == expectNumber and isLeaf:
            for i in path:
                res.append(i.val)
            Res.append(res)
        #如果不是叶节点，则遍历它的子节点
        if root.left:
            Res = self.Find_Path(root.left, expectNumber, path, Res)
        if root.right:
            Res = self.Find_Path(root.right, expectNumber, path, Res)
        #再返回父节点之前，在路径上删除当前节点
        path.pop()
        return Res
            
