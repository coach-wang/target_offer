'''
1.在树A中找到和树B一样的节点R
2.判断树A中以R为根节点的子树是不是包含和树B一样的结构
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not isinstance(pRoot1, TreeNode) or not isinstance(pRoot2, TreeNode):
            return False
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1HaveTree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result
    
    def DoesTree1HaveTree2(self, pRoot1, pRoot2):
        #如果从HasSubTree进入此函数，两指针都不会为空。所以当pRoot2为空时，说明遍历到了原来pRoot2的末尾，迭代结束。
        if not pRoot2:
            return True
        #当pRoot2不空，而pRoot1为空，说明不相等
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.DoesTree1HaveTree2(pRoot1.left, pRoot2.left) and self.DoesTree1HaveTree2(pRoot1.right, pRoot2.right)
    
