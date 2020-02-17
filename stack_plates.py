# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 20:46:46 2019

@author: srinath
"""

class Stack:
    def __init__(self,capacity):
        self.items = []
        self.capacity=capacity

    def push(self, item):
        if self.items==[]:
            self.items.append([item])
        else:
            if(len(self.items[-1])>=self.capacity):
                self.items.append([item])
            else:
                self.items[-1].append(item)

    def pop(self):
        pop=self.items[-1][-1]
        if(len(self.items[-1])==1):
            del self.items[-1]
        else:
            del self.items[-1][-1]
        return pop
    
    #def popAt(self,index):
     #   pop=self.items[index-1][-1]
        

if __name__=="__main__":
    s=Stack(3)
    s.push(3)
    s.push(3)
    s.push(4)
    print(s.items)
    print(s.pop())
    #print(s.pop())
    print(s.items)