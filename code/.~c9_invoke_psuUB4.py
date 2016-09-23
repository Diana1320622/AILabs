import sys
import networkx as nx
import copy

if len(sys.argv) == 2:
    while boxes:
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
    diccionarioStacks = {} #donde siempre esta el estado nuevo
    diccionarioGoal = {}
    
    
    #fill diccionarioionary with start
    for j in range(0,len(containers)):
        diccionarioStacks[j] = []
        diccionarioGoal[j] = []
    print ("test")
    print diccionarioStacks
    print diccionarioGoal
    G = nx.Graph(stacks = diccionarioStacks )
    i=0
    for pair in containers:
        diccionarioStacks[i].append(pair)
        i = i+1
    i=0
    #fill diccionarioionary with goal
    for pair in final
        diccionarioGoal[i].append(pair)
        i = i+1
    
    # print diccionarioStacks
    # print diccionarioGoal
    nodeCount = 1
    G.add_node(nodeCount, stacks=diccionarioStacks)
    nodeCount = nodeCount+1
    lengthStack = []
    moveStack = [] #(start,finish)
    
    #empty container
    for key in diccionarioStacks:
        if '' in diccionarioStacks[key]:
            lengthStack.append(0)
        else:
            lengthStack.append(len(diccionarioStacks[key]))
    
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
        print diccionarioStacks
        newStack = {}
        newStack = copy.deepcopy(diccionarioStacks)
        # newStack = diccionarioStacks.copy()
        aux = move.split(',')
        fin = int(aux[1])
        orig = int(aux[0])
        # print newStack[orig].pop()
        if '' in newStack[fin]:
            newStack[fin].append(newStack[orig].pop())
            ind = newStack[fin].index('')
            newStack[fin].pop(ind)
        else:
            newStack[fin].append(newStack[orig].pop())
        G.add_node(nodeCount, stacks=newStack)
        print("new stack")
        print newStack
        nodeCount = nodeCount+1
    
    # G.add_node(nodeCount, stacks=diccionarioStacks)
    # diccionarioStacks[2].append(diccionarioStacks[0].pop())
    # G.add_node(2, stacks=diccionarioStacks)
    # G.add_edge(1, 2, weight=3)
    print ("graph")
    print G.graph
    # print ("node")
    print G.node(data=True)
    
else:
    print("Invalid input")
