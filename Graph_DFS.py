# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 12:26:11 2019

@author: srinath
"""

class Queue:
    def __init__(self):
        self.items1 = []
        self.items2=[]

    def push(self,item):
        self.items1.append(item)
            

    def pop(self):
        while(self.items1!=[]):
            self.items2.append(self.items1[-1])
            del self.items1[-1]
        return self.items2
    
    def peek(self): 
        if (self.items1==[]): 
            return -1 # return minus infinite 
        return self.items1[-1]

class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)
            

    def peek(self):
        pop=self.items[-1]
        return pop
    
    def pop(self):
        if(self.items==[]):
            return -1
        del self.items[-1]
        return self.items

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def DFS(self,root):
        visited=[root]
        poplist=[]
        
        s.push(root)
        #values=self.__graph_dict.get(root)
        
        while(s.items != []):
            if self.__graph_dict.get(s.peek())==[]:
                poplist.append(s.peek())
                s.pop()
            else:
                len1 = len(s.items)
                for element in self.__graph_dict.get(s.peek()):  
                    if element not in visited:
                        visited.append(element)
                        s.push(element)
                if len1 == len(s.items):
                    poplist.append(s.peek())
                    s.pop()
                        
        
        print(poplist)
                    
        '''for node in self.__graph_dict.get(root):
            if(s.pop()!=node):
                self.DFS(node)  ''' 
                
                
                
        
        
        
    
    
if __name__=="__main__":
    g={'0':['1','4','5'],
       '1':['4','3'],
       '2':[],
       '3':['4','2'],
       '4':[],
       '5':[]
       }
    
    q=Queue()
    s=Stack()
    graph=Graph(g)
    
    print(list(g.keys())[0],g)
    root=list(g.keys())[1]
    graph.DFS(root)
    

        
        
        