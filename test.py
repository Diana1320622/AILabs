import sys
import networkx as nx

dictStacks = dict() #donde siempre esta el estado nuevo


G = nx.Graph(stacks=dictStacks)
# dictStacks[0].append('A')
# dictStacks[0].append('B')
# dictStacks[1].append('C')
print dictStacks
# G.add_node(1, stacks=dictStacks)
# dictStacks[2].append(dictStacks[0].pop())
# print dictStacks
# G.add_node(2, stacks=dictStacks)
# G.add_edge(1, 2, weight=3)
# print G.nodes(data=True)