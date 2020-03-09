'''
如果题目要求处理一颗二叉树的遍历序列，则可以先找到二叉树的根节点，
再基于根节点把整棵树的遍历序列拆分成左子树对应的子序列和右子树对应的子序列，接下来在递归地处理这两个子序列
'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        root = sequence[-1]
        length = len(sequence)
        #左子树
        i = 0
        while i < length - 1:
            if sequence[i] > root:
                break
            i += 1
        #右子树
        j = i
        while j < length - 1:
            if sequence[j] < root:
                return False
            j += 1
        #判断左子树是不是二叉搜索树
        left = True
        if i > 0: #说明sequence不为空，如果i=0，那么没有左子树
            left = self.VerifySquenceOfBST(sequence[:i])
        #判断右子树是不是二叉搜索树
        right = True
        if i < length - 1:#如果等于，没有右子树
            right = self.VerifySquenceOfBST(sequence[i:length-1])
        return left and right
