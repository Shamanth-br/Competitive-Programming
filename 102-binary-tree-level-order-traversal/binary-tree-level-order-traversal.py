# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        ans = []
        i, j, count = 0, 0, 0
        queue.append(root)
        while(i<=j):
            curr_level = []
            count = 0
            if root == None:
                return []
            
            while(i <= j):
                curr_level.append(queue[i].val)
                if queue[i].left:
                    queue.append(queue[i].left)
                    count += 1
                if queue[i].right:
                    queue.append(queue[i].right)
                    count += 1 
                i += 1
            ans.append(curr_level)
            j += count
        return ans