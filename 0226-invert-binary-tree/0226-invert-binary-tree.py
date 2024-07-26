class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            left = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(left)
        return root