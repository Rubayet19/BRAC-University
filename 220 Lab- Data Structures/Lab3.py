class Node:
    def __init__(self, element, next, prev):
        self.element=element
        self.next=next
        self.prev=prev

class DummyHeadedDoublyCircularLinkedList:
    def __init__(self,a):
        if a is not None:
            self.head=Node(None,None,None)
            tail=Node(a[0],None,None)
            self.head.next=tail
            tail.next=self.head
            self.head.prev=tail
            tail.prev=self.head

            for i in range(1,len(a)):
                newNode=Node(a[i],None,None)
                tail.next=newNode
                newNode.prev=tail
                tail=tail.next
            tail.next=self.head

    def showList(self):
        n=self.head.next
        if n!=None:
            while n is not self.head:
                print(n.element)
                n=n.next
        else:
            print("Empty List")


    def insert(self, newElement):
        newNode=Node(newElement,None,None)
        n=self.head.next
        while n is not self.head:
            if n.element==newElement:
                Print("Key already exists")
                return
            n=n.next
            
        n=self.head.next
        while(n.next!=self.head):
            n=n.next
        n.next=newNode
        newNode.prev=n
        newNode.next=self.head
        self.head.prev=newNode

    def insert2(self,newElement,index):
        newNode=Node(newElement,None,None)
        n=self.head.next
        count=0
        check=False
        if n is not None:
            while n is not self.head:
                count+=1
                n=n.next
            if (index<0 or index>=count):
                raise Exception("Invalid index")
                return
            
            n=self.head.next
            while n is not self.head:
                if n.element==newElement:
                    print("Key already exists")
                    check=True
                    break
                n=n.next
                
            if check==False:
                if index==0:
                    t=self.head.next
                    self.head.next=newNode
                    newNode.prev=self.head
                    newNode.next=t
                    t.prev=newNode

                else:
                     j=0
                     while j<index:
                         n=n.next
                         j+=1
                     s=n.next
                     n.next=newNode
                     s.prev=newNode
                     newNode.prev=n
                     newNode.next=s
    
    def remove(self,index):
      n=self.head.next
      count=0
      check=False
      if n is not None:
            while n is not self.head:
                count+=1
                n=n.next
            if (index<0 or index>=count):
                raise Exception("Invalid index")
                return
            
      n=self.head
      if index==0:
          rem=self.head.next
          n.next=rem.next
          rem.next.prev=self.head
          rem.element=None
          rem.next=None
          rem.prev=None
      elif index==count-1:
          rem=self.head.prev
          self.head.prev=rem.prev
          rem.prev.next=self.head
          rem.element=None
          rem.next=None
          rem.prev=None
      else:
          j=0
          while j<index+1:
              n=n.next
              j+=1
          rem=n
          rem.prev.next=rem.next
          rem.next.prev=rem.prev
          rem.element=None
          rem.next=None
          rem.prev=None
        
    def removeKey(self, deletekey):
        n=self.head.next
        if n.element==deletekey:
            temp=n.element
            self.head.next=n.next
            n.next.prev=self.head
            n.element=None
            n.next=None
            n.prev=None
            return temp
        n=self.head.next
        while n is not self.head:
            if n.element==deletekey:
                temp=n.element
                n.prev.next=n.next
                n.next.prev=n.prev
                n.element=None
                n.next=None
                n.prev=None
                return temp
            
            if n.element==self.head.prev:
                temp=n.element
                self.head.prev=n.prev
                n.prev.next=self.head
                n.element=None
                n.next=None
                n.prev=None
                return temp
    
            n=n.next








        


        





        





            


