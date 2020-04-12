class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def levelOrder(root):
    visited = []
    if (root is None):
        return

    visited.append(root)
    while (len(visited) > 0):
        print (visited[0].info, end = " ")
        node_visited = visited.pop(0)
            
        if(node_visited.left != None):
            visited.append(node_visited.left)

        if(node_visited.right != None):
            visited.append(node_visited.right)

# Time Complexity: O(n), Space Complexity: O(n)
# Where n is number of nodes in the binary tree       

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)