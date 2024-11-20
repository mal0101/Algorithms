# This code enables you to check if a binary tree is balanced or not.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # Helper function to calculate height and check balance
        def checkHeight(node):
            if not node:
                return 0  # Height of an empty subtree is 0

            # Recursively check the height of the left subtree
            leftHeight = checkHeight(node.left)
            if leftHeight == -1:
                return -1  # Left subtree is not balanced

            # Recursively check the height of the right subtree
            rightHeight = checkHeight(node.right)
            if rightHeight == -1:
                return -1  # Right subtree is not balanced

            # Check if the current node is balanced
            if abs(leftHeight - rightHeight) > 1:
                return -1  # Current node is not balanced

            # Return the height of the current subtree
            return max(leftHeight, rightHeight) + 1

        # The tree is balanced if checkHeight(root) does not return -1
        return checkHeight(root) != -1