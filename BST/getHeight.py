class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        def height(node):
            if not node:
                return -1
            else:
                return 1 + (height(node.left) if height(node.left) >= height(node.right) else height(node.right))
        return height(root)

# T=int(input())
myTree=Solution()
root = None
a = [3, 5, 2, 1, 4, 6, 7]
# for i in range(T):
for i in a:
    # data=int(input())
    # root=myTree.insert(root,data)
    root=myTree.insert(root,i)
height=myTree.getHeight(root)
print(height)     