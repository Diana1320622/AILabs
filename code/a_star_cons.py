#A* search consistent heuristic
import sys

#define heuristic
#def heuristic():

#implement algorithm
#def a_search(graph, start, goal):

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
    
    print(containers)
    if containers[2] == None:
        print("empty")
    else:
        print("not empty")
    
    #clean goal
    goalClean = goal.replace("(", "")
    goalClean = goalClean.replace(")", "")
    final = goalClean.split('; ')
    if '' in containers:
        index = containers.index('')
        containers.pop(index)
        containers.insert(index,[])
    else:
        print("not ")
    print(containers)
   
    cont1 = len(containers[1])
    
   
    
    xs = ["(1,2)", "(0,1)", "(1,0)", "(2,1)"]
    
    
    # if "(1,2)" in xs:
    #     print("true")
    # else:
    #     print("false")

    # print(height)
    # print(start)
else:
    print("Invalid input")