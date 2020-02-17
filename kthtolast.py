# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:32:25 2019

@author: srinath
"""

class Node:
#    def __init__(self,data,nextNode=None):
#        self.data=data
#        self.nextNode=nextNode

    def __init__(self,data,nextNode):
        self.data = data
        self.nextNode = None
        
#    4
def printList(l):
    value = []
    while(l):
        value.append(l.data)
        l = l.nextNode
    print(' -> '.join(map(str, value)))

def getsize(l1):
    s=1
    p1=l1
    while(p1.nextNode!=None):
        s=s+1
        p1=p1.nextNode
    return s

def ktolast(l1,k):
    p1=l1
    p2=l1
    
    for i in range(0,k):
        p2=p2.nextNode
    
    if(p2.nextNode==None):
        return p1.data
    
    else:
        while(p2.nextNode!=None):
            p1=p1.nextNode
            p2=p2.nextNode
        return p1.data



if __name__=="__main__":
     
#    l1 = Node(9, Node(8, Node(5)))
    l1 = Node(5,None)
    l2= Node(8,None)
    l1.nextNode=l2
    l3= Node(9,None)
    l2.nextNode=l3
    #    l = []
    #    l.append(Node(9,None))
    #    l[1].data
    #    l2 = Node(9,None)
    #    print(l2.data)    
    #    l3= Node(8,None)
    #    l2.assigner(l3)
    ##    l2.nextNode=l3   
    #    print(l2.nextNode.data)
    #    l4 = Node(5,l3)
    #    l3.nextNode=l4
    printList(l1)
    print(l1.nextNode)
#    for(i in range(1,5)):
#        
#    print(l4.data)
    k=2
    size=getsize(l1)
    print(size)
    #print(size)
    
    if(k<size):
        element=ktolast(l1,k)
        print(element)
    else:
        print("K should be smaller than size of linkedlist")
#    
    
#    
    
    