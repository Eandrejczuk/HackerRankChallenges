
# https://www.hackerrank.com/challenges/30-linked-list-deletion/problem

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        if not head or not head.next:
            return head
        else:
            if head.data == head.next.data:
                head.next = head.next.next
                self.removeDuplicates(head)
            else:
                self.removeDuplicates(head.next)
            return head

mylist= Solution()
T=6
data_table = [1, 2, 2, 3, 3, 4]

head=None
for i in range(T):
    data=data_table[i]
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head)