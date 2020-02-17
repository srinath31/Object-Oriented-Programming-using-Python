class Stack:
    def __init__(self):
        self.items = []
        #self.mini=0
    def push(self,item):
        mini2=item
        if(self.items==[]):
            self.items.append(item)
        else:
            if(self.items[-1]<mini2):
                p=self.items.pop()
                self.items.append(item)
                self.items.append(p)
            else:
                self.items.append(item)
            

    def mini(self):
        pop=self.items[-1]
        return pop

if __name__=="__main__":
    s=Stack()
    s.push(80)
    s.push(2)
    s.push(25)
    s.push(26)
    s.push(1)
    print(s.mini())
    print(s.items)
    