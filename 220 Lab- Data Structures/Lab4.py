class Stack:
    stack=[]
    pointer=-1
    
    def parenthesis_checker(self, text):
        counter=0
        temp=[]
        for i in text:
            counter+=1
            if i in ["[","{","("]:
                self.stack[len(self.stack):]=[i]#drujh
                self.pointer+=1
                temp[len(temp):]=[counter]               
            if i in ["]","}",")"]:
                if not self.stack:#edgjkl
                    return print("Error at character #{}. '{}'- not opened.".format(counter,i))
                left_index=temp[-1]
                if self.stack:
                    left=self.stack[self.pointer]
                    self.stack=self.stack[:-1]#jnkl
                    self.pointer-=1
                    temp=temp[:-1]
                    
                    if left == '[' and i==']':
                        continue
                    elif left == '{' and i=='}':
                        continue
                    elif left == '(' and i==')':
                        continue
                    else:
                        return print("Error at character #{}. '{}'- not closed.".format(left_index,left))                       
                    
        if self.pointer==-1:
            return print("The expression is correct.")
 


Stack().parenthesis_checker("1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")

#-----------------------------------------------------------------------------------------

class Node:
    def __init__(self, data,index):
        self.data = data
        self.index = index
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data,index):

        if self.head == None:
            self.head = Node(data,index)
        else:
            newnode = Node(data,index)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isempty():
            return None

        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data , self.head.index

def parenthesis_checker(text):
    bracket_stack = Stack()
    counter=0
    for i in text:
        counter+=1
        if i in ["[","{","("]:
            bracket_stack.push(i,counter)

        if i in ["]","}",")"]: 
            if bracket_stack.isempty():
                return print("Error at character #{}. '{}'- not opened.".format(counter,i))                
               
            left , left_index= bracket_stack.peek()
            
            if not bracket_stack.isempty():
                bracket_stack.pop()
                if left == '[' and i==']':
                       continue
                elif left == '{' and i=='}':
                    continue
                elif left == '(' and i==')':
                    continue
                else:
                    return print("Error at character #{}. '{}'- not closed.".format(left_index,left))
                    
                
    return print("The expression is correct.")
          

parenthesis_checker("1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")