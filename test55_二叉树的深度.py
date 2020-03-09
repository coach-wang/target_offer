#1 二叉树的深度
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        #n = max(n左， n右) + 1
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        
        return max(left, right)+1

#2 平衡二叉树
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    #后序遍历
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return self.balanceHeight(pRoot) >= 0
    
    def balanceHeight(self, root):
        if not root:
            return 0
        left = self.balanceHeight(root.left)
        right = self.balanceHeight(root.right)
        
        if (left<0 or right<0 or abs(left-right)>1):
            return -1
        return max(left, right)+1
