class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    # def insert_head(self, data):
    #     newNode = Node(data)
    #     if (self.head != None):
    #         newNode = self.head
    #     self.head = newNode

    def insert(self,head,data):
        if (head is None):
            head = Node(data)
            head.data = data
        else:
            temp = head
            while(temp.next != None):
                temp = temp.next
            temp.next = Node(data)
        return (head)
      
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  