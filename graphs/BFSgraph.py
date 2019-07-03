#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:34:57 2019

@author: abhijithneilabraham
"""

from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    def bfs(self,s):
        #mark all the vertices as not visited or we wont know if  a node is visited already or not
        visited=[False]*(len(self.graph))
        #create a queue for bfs
        queue=[]
        # Mark the source node as  
        # visited and enqueue it
        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0) #dequeue a vertex from queue and print it
            print(s,end=" ")
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
g=Graph()
g.addedge(0,1)
g.addedge(0, 2) 
g.addedge(1, 2) 
g.addedge(1, 3) 
g.addedge(1, 4) 
g.addedge(4, 4) 
  
print("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
g.bfs(2) 
        
        
        