# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        #原先指向左子节点的指针调整为链表中指向前一节点的指针，指向右子节点的指针调整为指向后一节点
        if pRootOfTree == None:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        #处理左子树
        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left
        #连接根与左子树最大节点
        if left:
            while left.right:
                left = left.right
            pRootOfTree.left, left.right = left, pRootOfTree
        #处理右子树
        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right
        #连接根与右子树最小节点
        if right:
            while right.left:
                right = right.left
            pRootOfTree.right, right.left = right, pRootOfTree
        
        while(pRootOfTree.left):
            pRootOfTree = pRootOfTree.left
        return pRootOfTree
