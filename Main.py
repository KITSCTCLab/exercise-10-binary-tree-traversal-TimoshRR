class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class BST:
    def insert(root, data) -> BinaryTreeNode:
        """If binary search tree is empty, make a new node, declare it as root and return the root.
            If tree is not empty and if new_value is less than value of data in root, add it to left subtree and proceed recursively.
            If tree is not empty and if new_value is >= value of data in root, add it to right subtree and proceed recursively.
            Finally, return the root.
            """
        # Write your code here
        if root==None:
                new_node=node(key)
                self.root=new_node
                return self.root
            if self.root>data:
                self.root.left=self.insert(self.root.left,data)

            else:
                self.root.right=self.insert(self.root.right,data)


    def inorder(root) -> None:
        # Write your code here
        if root:
            inorder(root.left)
 
        # then print the data of node
            print(root.data)
 
        # now recur on right child
           inorder(root.right)


    def preorder(root) -> None:
        # Write your code here
        if root:
 
        # First print the data of node
            print(root.data)
 
        # Then recur on left child
            preorder(root.left)
 
        # Finally recur on right child
            preorder(root.right)


    def postorder(root) -> None:
        # Write your code here
        if root:
 
        # First recur on left child
            postorder(root.left)
 
        # the recur on right child
            postorder(root.right)
 
        # now print the data of node
            print(root.data)


# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)
