from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        
        # Step 1: Find the maximum value and its index
        max_val = max(nums)
        idx = nums.index(max_val)

        # Step 2: Create the root node with the maximum value
        root = TreeNode(max_val)
        
        # Step 3: Recursively build the left and right subtrees
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])
        
        return root

# --- Helper function to visualize the output (Level Order Traversal) ---
def print_tree(root):
    if not root:
        print("[]")
        return
    
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Trim trailing None values for a cleaner look
    while result and result[-1] is None:
        result.pop()
    print(result)

# --- Execution ---
nums = [3, 2, 1, 6, 0, 5]
sol = Solution()
tree_root = sol.constructMaximumBinaryTree(nums)

print("Input array:", nums)
print("Maximum Binary Tree (Level Order):", end=" ")
print_tree(tree_root)