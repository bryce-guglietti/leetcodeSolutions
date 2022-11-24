# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # global variable to hold the diameter
        result = [0]

        # inner function for a depth first search 
        def dfs(node):
            # if the node being reached is none return -1
            if not node:
                return -1
            # go as far left and right as possible (traverse tree)
            left = dfs(node.left)
            right = dfs(node.right)

            # update global result to the max height between 
            # the current aresult and the current left and right values
            result[0] = max( result[0], (2 + left + right ))

            #return the max height between left and right and add 1
            return 1 + max( left, right )
        
        # call search 
        dfs(root)

        #return the result 
        return result[0]
