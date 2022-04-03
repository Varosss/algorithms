# 104. Maximum Depth of Binary Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, node):
        depth = 1
        leftDepth = 0
        rightDepht = 0

        if not node:
            return 0
        
        if node.left:
            leftDepth += Solution().maxDepth(node.left)
        
        if node.right:
            rightDepht += Solution().maxDepth(node.right)

        depth += max(leftDepth, rightDepht)
        
        return depth


def addElementInTree(element, node):
    root = node

    if not node:
        node = TreeNode(element)

    if element < node.val:
        if not node.left:
            node.left = TreeNode(element)
        
        if node.left:
            return addElementInTree(element, node.left)

    if element > node.val:
        if not node.right:
            node.right = TreeNode(element)

        if node.right:
            return addElementInTree(element, node.right)
    
    return root


def showTreeElements(node):
    if not node:
        return None
    
    if node.left:
        showTreeElements(node.left)

    print(node.val)

    if node.right:
        showTreeElements(node.right)


def makeTree(list):
    root = TreeNode()

    for i in range(len(list)):
        if i == 0:
            root = addElementInTree(list[0], root)

        else:
            addElementInTree(list[i], root)

    return root

list = [9, 3, 6, 4, 1, 8]
root = makeTree()
print(Solution().maxDepth(root))