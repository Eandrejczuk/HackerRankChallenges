import sys

# https://www.hackerrank.com/challenges/30-binary-trees/problem

class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        q = [root]

        for node in q:
            if node:
                print(node.data, end=' ')

                q.append(node.left)
                q.append(node.right)


T = 6
data_table = [3, 5, 4, 7, 2, 1]

myTree = Solution()
root = None
for i in range(T):
    data = data_table[i]
    root = myTree.insert(root, data)
myTree.levelOrder(root)
