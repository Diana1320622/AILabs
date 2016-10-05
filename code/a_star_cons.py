import sys
import operator
import re
from collections import deque
from cStringIO import StringIO
# a*
#cost f(n) = g + h
#push the root into the stack 
#need open, visited and successors list 

pathStack = []
stateQueue = deque([])
visitedStack = [] #nodes visited
successors = []
weightStack = []
costDictionary = {}
orderedSuccesors = [];
auxOrderedSuccesors = [];
nodeList = []
class Node(object):
    def __init__(self):
        self.problem = None #current node (contxainers) list
        self.parent = None
        self.action = None
        self.H = 0
        self.G = 0
        self.F = 0

def childNode(problem, parent, action, h, g, f):
    node = Node()
    node.action = action
    node.parent = parent
    node.problem = problem
    node.H = h
    node.G = g
    node.F = f
    
    # acumG = 0
    # #calculate G based on the Gs above
    # for visited in visitedStack:
    #     acumG = acumG + visited.G + (1+h)
    
    # node.G = acumG
    # node.F = node.G + node.H
    
    return node

def calculateG(h):
    acumG = 0
    #calculate G based on the Gs above
    for visited in visitedStack:
        acumG = acumG + visited.G + (1+h)
    
    return acumG
        
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
 
 
#eturn the list of direct descendants in shortest total estimation order
def totalSuccesors(currentNode):
    return

def lookforNode(n):
    # print "checkvisitedstack:",len(visitedStack)
    for visit in visitedStack:
        # print "valuecheck:",visit.problem
        if visit.problem == n.problem:
            # print "found!"
            return True
        
    return False

def checkGoal(node,goal):
    count = 0
    for pair in goal:
        if pair != 'X':
            if node.problem[count] != pair:
                return False
        else:
            count = count+1
    return True     
    
def a_star(stateQueue, start, goal):
    
    #while the stack is not empty
    #   remove the last node in the stack
    #   insert node in visited
    #   check if it is the goal
    #   if not, return the list of direct descendants in shortest total estimation order
    #   for each element into the list
    #       check if it isnt in visited list
    
    #           insert in open list
    
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
        #print 'popped node move:',aux.action
        #print 'popped node F:',aux.F
        pathStack.append(aux.action) #movements done
        visitedStack.append(aux) #visited nodes
            
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
                                h = abs(res-x) 
                                weightStack.append(h);
                else:
                    xCount = xCount+1
    
            #print 'moveStack:',moveStack                    
            #add nodes to the queue
            countWeights = 0
            for move in moveStack:
                #get the array in order of shortest estimation to largest
                costDictionary[move] = weightStack[countWeights]+calculateG(weightStack[countWeights]) #this is the key as the move and the values as F (h+g)
                countWeights = countWeights + 1
            
            nodeList = sorted(costDictionary.items(), key=lambda x:x[1]) #h value
            #print "nodelist:", nodeList 
            
            countWeights = 0
            for pair in nodeList:    
                newNode = childNode(createList(pair[0],aux.problem),aux,move,weightStack[countWeights],calculateG(weightStack[countWeights]),pair[1])
                countWeights = countWeights + 1
                #print 'new:',newNode.problem
                #print 'g: ', newNode.G
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
    
    root = childNode(containers, None, None, 0,0,0)
    stateQueue.append(root)
    
    if a_star(stateQueue, containers, final):
        #print '\n\tSOLUTION'
        print moveCount
        #solution = [i for i in pathStack if isinstance(i, (inre.sub('[^0-9]', '', pathStack)
        #print pathStack
        #print '(',solution,')'
        pathStack.pop(0)
        path = StringIO()
        # print pathStack
        for p in range(0,len(pathStack)):
            if p == len(pathStack)-1:
                path.write("("+pathStack[p]+")")
            else:
                path.write("("+pathStack[p]+")")
                path.write(",")
        print path.getvalue()
        
    else:
        print '\n\t NO SOLUTION FOUND \n'
else: 
    print("Invalid Input")

#run like this: python a_star_cons.py dummy1.in
