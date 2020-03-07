'''
1.如果该节点有右子树，则它的下一个节点就是右子树的最左子节点
2.该节点无右子树，如果该节点是父节点的左子节点，则下一节点是父节点；否则向上遍历，
  直到找到一个节点是它父节点的左子节点，则下一节点是这个节点的父节点（找不到就说明这个节点没有下一个节点了）
'''


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode == None:
            return
        cur = pNode
        if pNode.right:
            cur = pNode.right
            while cur.left:
                cur = cur.left
            return cur
        while cur.next:
            if cur == cur.next.left:
                return cur.next
            cur = cur.next
