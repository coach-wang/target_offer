# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    flag = -1
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)
    
    def Deserialize(self, s):
        # write code here
        l = s.split(',')
        root = None
        root = self.deserial(l)
        return root

    def deserial(self, l):
        self.flag += 1
        if self.flag >= len(l):
            return None
        
        root = None
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.deserial(l)
            root.right = self.deserial(l)
        return root
