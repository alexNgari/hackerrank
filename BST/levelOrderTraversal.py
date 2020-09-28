import sys

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

    def levelOrder(self,root):
        #Write your code here
        from collections import deque
        queue = deque()
        queue.append(root)
        while len(queue) != 0:
          node = queue.popleft()
          if node.left: queue.append(node.left)
          if node.right: queue.append(node.right)
          print(node.data, end=" ")

# T=int(input())
myTree=Solution()
root = None
a = [3, 5, 4, 7, 2, 1]
# for i in range(T):
for i in a:
    # data=int(input())
    # root=myTree.insert(root,data)
    root = myTree.insert(root, i)
myTree.levelOrder(root)
