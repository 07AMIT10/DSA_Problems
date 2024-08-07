#{ 
 # Driver Code Starts
#Initial Template for Python 3
# 
# } Driver Code Ends
#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class Solution:
#     def is_sum_tree(self, node):
#         # Base case: If the node is None or a leaf node (has no children),
#         # it is considered a Sum Tree, so we return True.
#         if node is None or (node.left is None and node.right is None):
#             return True

#         # If the current node's data is not equal to the sum of its
#         # left and right subtrees, it is not a Sum Tree, so we return False.
#         if node.data != (0 if node.left is None else node.left.data) + (0 if node.right is None else node.right.data):
#             return False

#         # Recursively check the left and right subtrees.
#         return self.is_sum_tree(node.left) and self.is_sum_tree(node.right)
        
        
class Solution:
    def check_sum(self,node):
        if node is None:
            return True, 0
        if node.left is None and node.right is None:
            return True, node.data
        is_left, left_sum=self.check_sum(node.left)
        is_right, right_sum=self.check_sum(node.right)
        
        
        curr=is_left and is_right and (node.data== left_sum+ right_sum)


        return curr, left_sum+right_sum+node.data

    def is_sum_tree(self, node):
        is_true, _=self.check_sum(node)
        
        return is_true

#{ 
 # Driver Code Starts.
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Utility function to create a new Tree Node
def new_node(val):
    return Node(val)


# Function to Build Tree
def build_tree(s):
    # Corner Case
    if not s or s[0] == 'N':
        return None

    # Creating list of strings from input string after splitting by space
    ip = s.split()

    # Create the root of the tree
    root = new_node(int(ip[0]))

    # Push the root to the queue
    queue = []
    queue.append(root)

    # Starting from the second element
    i = 1
    while queue and i < len(ip):
        # Get and remove the front of the queue
        curr_node = queue.pop(0)

        # Get the current node's value from the string
        curr_val = ip[i]

        # If the left child is not null
        if curr_val != "N":
            # Create the left child for the current node
            curr_node.left = new_node(int(curr_val))

            # Push it to the queue
            queue.append(curr_node.left)

        # For the right child
        i += 1
        if i >= len(ip):
            break
        curr_val = ip[i]

        # If the right child is not null
        if curr_val != "N":
            # Create the right child for the current node
            curr_node.right = new_node(int(curr_val))

            # Push it to the queue
            queue.append(curr_node.right)
        i += 1

    return root


# Driver code
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = build_tree(s)
        ob = Solution()
        if ob.is_sum_tree(root):
            print("true")
        else:
            print("false")

# } Driver Code Ends