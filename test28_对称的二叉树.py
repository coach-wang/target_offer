class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        #if not isinstance(pRoot, TreeNode):
            #return False  #输入为空也算对称？
        return self.is_Symmetrical(pRoot, pRoot)
    
    def is_Symmetrical(self, pRoot1, pRoot2):
        if not pRoot1 and not pRoot2:
            return True
        elif not pRoot1 or not pRoot2:
            return False
        elif pRoot1.val != pRoot2.val:
            return False
        return self.is_Symmetrical(pRoot1.left, pRoot2.right) and self.is_Symmetrical(pRoot1.right, pRoot2.left)
    
