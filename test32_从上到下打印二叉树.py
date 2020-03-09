#01 不分行从上到下打印二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        #if not isinstance(root, TreeNode):
            #return
        if not root:
            return []
        queue = []
        queue.append(root)
        tree = []
        while queue:
            temp = queue.pop(0)
            tree.append(temp.val)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return tree

#02分行从上到下打印二叉树
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        temp = [pRoot]
        while temp:
            size = len(temp)
            row = []
            for i in temp:
                row.append(i.val)
            res.append(row)
            for i in range(size):
                node = temp.pop(0)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
        return res

#03 之字形打印二叉树
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        stack1= [pRoot]
        nextstack = []
        tree = []
        subtree = []
        current = 0
        while stack1:
            temp = stack1.pop()
            subtree.append(temp.val)
            if current == 0:
                #奇数层，先压入左子节点
                if temp.left:
                    nextstack.append(temp.left)
                if temp.right:
                    nextstack.append(temp.right)
            else:
                #偶数层，先压入右子节点
                if temp.right:
                    nextstack.append(temp.right)
                if temp.left:
                    nextstack.append(temp.left)
            if not stack1:
                #该层打完了
                current = 1 - current
                stack1 = nextstack
                nextstack = []
                tree.append(subtree)
                subtree = []
        return tree
                    

