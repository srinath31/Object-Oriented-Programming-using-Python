# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:39:01 2019

@author: srina
"""

class Queue:
    def __init__(self):
        self.items1 = []
        self.items2=[]

    def push(self,raapchik):
        self.items1.append(raapchik)
            

    def pop(self):
        while(self.items1!=[]):
            self.items2.append(self.items1[-1])
            del self.items1[-1]
        return self.items2
    
    def peek(self): 
        while(self.items1!=[]):
            self.items2.append(self.items1[-1])
            del self.items1[-1]
        return self.items2[-1]
    

if __name__=="__main__":
    q1=Queue()
    q1.push(80)
    q1.push(2)
    q1.push(25)
    q1.push(26)
    q1.push(1)
    #q1.pop()
    print(q1.peek())