# 94. Binary Tree Inorder Traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, node):
        if not node:
            return []

        def traversal(node, list):
            if node.left:
                traversal(node.left, list)

            list.append(node.val)

            if node.right:
                traversal(node.right, list)

            return list

        answer = traversal(node, [])

        return answer

# list = [6, 4, 7, 8, 9, 10, 3, 1, 2]

node = TreeNode(5)
root = node
root.left = TreeNode(3)
root.right = TreeNode(7)
print(Solution().inorderTraversal(root))