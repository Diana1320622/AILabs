import sys
from collections import deque

pathStack = [] 
visitedStack = [] #nodes that were already visited
stateQueue = deque([])
state = 1
mopoveCount = 0

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
    
def checkGoal(node,goal):
    count = 0
    for pair in goal:
        if pair != 'X':
            if node.problem[count] != pair:
                return False
        else:
            count = count+1
    return True      
    

def createList(move, parentList):
    moves = move.split(',')
    origin = int(moves[0])
    end = int(moves[1])
    newList = []
    for letter in parentList: #copy parent list into newList
        newList.append(letter)
        
    potentialMove = newList.pop(origin).split(',') #get stack where the box to move is
    boxToMove = potentialMove.pop() #get box
    if len(potentialMove) <= 1:
        newList.insert(origin,''.join(potentialMove)) #return what was not taken from the stack
    else:
        newList.insert(origin,','.join(potentialMove))
        
    endList = newList.pop(end).split(',')#get the stack where the box will be moved
    if '' in endList:
        endList.insert(0,boxToMove)
        endList.pop()#add the box to the stack
    else:
        endList.append(boxToMove)#add the box to the stack

    newList.insert(end,','.join(endList)) #return the stack to the list
    return newList
    
    
def lookforNode(n):
    for node in visitedStack:
        if node.problem == n.problem:
            return True
        else:
            return False

def bfs(stateQueue, start, goal):
    #pop from stack
        #check if its goal
        #if not: apply every action posible to node and create a node for every action and add
        #it to the stack. You must check that the node has not been there before
        
    global moveCount # needs to be declared global 
    moveCount = 0
    
   # for i in range(0,3):
    while stateQueue:
        #print goal
        #print start
        lengthStack = []
        moveStack = [] #(start,finish)
        aux = stateQueue.popleft()
        moveCount = moveCount+1
        #add to the visited states
        #print 'popped node:',aux.problem
        pathStack.append(aux.action)
        visitedStack.append(aux)
            
        #check if the current state is the goal 
        if checkGoal(aux,goal):
            return True #return action and num of movements
        else:
            #get the length for each container
            for pair in aux.problem:
                if len(pair) > 1:
                    lengthStack.append(len(pair.split(',')))
                else:
                    lengthStack.append(len(pair))
                    
            # print 'lengthStack:',lengthStack
            xCount = 0
            for length in lengthStack:
                if length > 0: #agarrar
                    x = xCount
                    xCount = xCount+1
                    for res in range(0, len(lengthStack)):
                        if res != x:
                            if lengthStack[res] < height:
                                moveStack.append(str(x)+','+ str(res))
                else:
                    xCount = xCount+1
    
            #print 'moveStack:',moveStack                    
            #add nodes to the queue
            for move in moveStack:
                # print 'aux problem:', aux.problem
                newNode = childNode(createList(move,aux.problem),aux,move)
                #print 'new:',newNode.problem
                if not lookforNode(newNode):
                    stateQueue.append(newNode)
    return False            
            
    
#main
if len(sys.argv) == 2:
    inputs = sys.argv
    var = [line.rstrip('\n') for line in open(inputs[1])]
    height = var[0] #maximum height of stack
    start = var[1] #initial location of the containers
    goal = var[2] #goal state
    #clean start
    startClean = start.replace("(", "")
    startClean = startClean.replace(")", "")
    containers = startClean.split('; ')

    #clean goal
    goalClean = goal.replace("(", "")
    goalClean = goal.replace("(", "")
    goalClean = goalClean.replace(")", "")
    final = goalClean.split('; ')
    
    
    root = childNode(containers, None, None)
    stateQueue.append(root)
    
    if bfs(stateQueue, containers, final):
        print '\n\tSOLUTION'
        print moveCount
        print pathStack
    else:
        print '\n\t NO SOLUTION FOUND \n'
else: 
    print("Invalid Input")