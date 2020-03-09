# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        #中序遍历
        self.result = []
        self.midnode(pRoot)
        if k <= 0 or len(self.result) < k:
            return None
        else:
            return self.result[k-1]
    
    def midnode(self, root):
        if not root:
            return 
        self.midnode(root.left)
        self.result.append(root)
        self.midnode(root.right)
