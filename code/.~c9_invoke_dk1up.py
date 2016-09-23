import sys
import networkx as nx
import copy

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
    goalClean = goalClean.replace(")", "")
    final = goalClean.split('; ')
    
    i = 0;
    dictStacks = dict() #donde siempre esta el estado nuevo
    dictGoal = dict()
    
    G = nx.Graph(stacks = dictStacks )
    #fill dictionary with start
    for pair in containers:
        dictStacks[i]=[pair]
        i = i+1
    i=0
    #fill dictionary with goal
    for pair in final:
        dictGoal[i]=[pair]
        i = i+1
    
    # print dictStacks
    # print dictGoal
    nodeCount = 0
    G.add_node(nodeCount, stacks=dictStacks)
    
    lengthStack = []
    moveStack = [] #(start,finish)
    
    #empty container
    for key in dictStacks:
        if '' in dictStacks[key]:
            lengthStack.append(0)
        else:
            lengthStack.append(len(dictStacks[key]))
    
    xCount = 0
    yCount = 0
    for length in lengthStack:
        if length > 0: #agarrar
            x = xCount
            xCount = xCount+1
            for res in range(0, len(lengthStack)):
                if res != x:
                    if lengthStack[res] < height:
                        moveStack.append(str(x)+','+ str(res))
                        
    for move in moveStack:
        print "original"
        print dictStacks
        newStack = dict()
        copy.deepcopy(dictStacks)
        # newStack = dictStacks.copy()
        aux = move.split(',')
        fin = int(aux[1])
        orig = int(aux[0])
        # print newStack[orig].pop()
        newStack[fin].append(newStack[orig].pop())
        G.add_node(nodeCount, stacks=newStack)
        print("new stack")
        print newStack
        nodeCount = nodeCount+1
        
        

    
    # G.add_node(nodeCount, stacks=dictStacks)
    # dictStacks[2].append(dictStacks[0].pop())
    # G.add_node(2, stacks=dictStacks)
    # G.add_edge(1, 2, weight=3)
    print ("graph")
    print G.graph
    print ("node")
    print G.node(data=True)

    
else:
    print("Invalid input")

    