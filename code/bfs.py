#!/usr/bin/env python
import sys

def bfs_paths(start,goal,graph):
    boxes = [(start, [start])]
    while boxes:
        (vertex, path) = boxes.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                boxes.append((next, path + [next])


#recibo argumentos
if len(sys.argv) == 4:
    arguments = sys.argv
    #lines = [line.rstrip('\n') for line in open(arguments[1])]
    height = int(float(arguments[2])) # altura
    start = str(arguments[3]) # start boxes
    goal = str(arguments[4]) # goal boxes
    
    #organize
    
    
else: 
    print ("wrong arguments, try again :)")
    