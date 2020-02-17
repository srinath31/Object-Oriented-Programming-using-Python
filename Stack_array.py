# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 16:17:14 2019

@author: srinath
"""

from sys import maxsize 
  
# Function to create a stack. It initializes size of stack as 0 
def createStack(): 
    stack = [] 
    return stack 
  
# Stack is empty when stack size is 0 
def isEmpty(stack): 
    return len(stack) == 0
  
# Function to add an item to stack. It increases size by 1 
def push(stack, item): 
    stack.append(item) 
    print(item) 
      
# Function to remove an item from stack. It decreases size by 1 
def pop(stack): 
    if (isEmpty(stack)): 
        return -1# return minus infinite 
      
    del stack[-1]
    return stack
  
# Function to return the top from stack without removing it 
def peek(stack): 
    if (isEmpty(stack)): 
        return -1 # return minus infinite 
    return stack[len(stack) - 1] 
  
# Driver program to test above functions     
stack1 = createStack() 
stack2=createStack()
stack3=createStack()

num_of_stacks=3

s=input("Enter the size of array: ")
size=int(s)

#if(size<3):
 #   print("array size should be at least 3")
#else:
splitposition=[]

splitposition.append(int(size/num_of_stacks))
splitposition.append(int((size/num_of_stacks)*2))
splitposition.append(int((size/num_of_stacks)*3))

length=0  
while(length!=size):
    if(length<splitposition[0]):
        push(stack1, length)
        length=length+1
    elif(length>=splitposition[0] and length<splitposition[1]):
        push(stack2,20)
        length=length+1
    else:
        push(stack3,30)
        length=length+1

print(splitposition)
print(stack1)
#print(stack2)
#print(stack3)
pop(stack1)
print(stack1)