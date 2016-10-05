import sys
from collections import deque
openQueue = deque([])
visitedQueue = []

class Node(object):
    def __init__(self):
        self.problem = None #current node (containers) list
        self.parent = None
        self.action = None

def childNode(problem, parent, action):
    node = Node()
    node.action = action
    node.parent = parent
    node.problem = problem
    return node
 
def lookforNode(n):
    
    for node in visitedQueue:
        if node.problem == n.problem and node.action == n.action:
            return True
        else:
            return False
    
def checkGoal(node,goal):
    count = 0
    for pair in goal:
        print 'pair:',pair
        if pair != 'X':
            if node.problem[count] != pair:
                return False
        else:
            count = count+1
                
    return True      
    


nodeTest = childNode(['A,B','C',''],[0,1],None)
nodeTest2 = childNode([0,1],['A','B',''],None)
dummyNode = childNode([1,2],['A','','B'],nodeTest)

list1 = ['A','B']

openQueue.append(nodeTest)
visitedQueue.append(nodeTest2)
openQueue.append(dummyNode)

poppedNode = openQueue.popleft()
if lookforNode(poppedNode):
    print ("Node is in the visitedQueue")
else:
    print ("Node is not in the visitedQueue")
    
testList = nodeTest.problem
toMove = testList.pop(0).split(',')
boxToMove = toMove.pop()
testList.insert(0,','.join(toMove))
print checkGoal(nodeTest,['X','A,B','X'])
print nodeTest.problem[1]

print testList