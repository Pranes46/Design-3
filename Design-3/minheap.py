class minheap:
    def __init__(self):
        self.heap=[]  #initializing the array
    def getmin(self):
        return self.heap[0]  #the minimum element will be stored in the index 0 and we are showing that in this function
        
    def bubbleup(self,index):
        parentindex = (index-1)//2  #to find the parent index 
        if parentindex<0:  #if the parent index val is 0 return nothing
            return
        if self.heap[parentindex]<self.heap[index]: #to checvk whether the index is greater than parent index
            return
        
        self.heap[parentindex],self.heap[index] = self.heap[index],self.heap[parentindex]  #we are swapping the new index value and parent index value
        
        self.bubbleup(parentindex)
        
    def bubbledown(self,index):
        leftchild = 2*index+1   # to find the index of the left child
        rightchild = 2*index+2   # to find the index of the right child
        temp = index   #we are storing the index in the temp variable
        
        
        if leftchild<len(self.heap) and self.heap[temp]>self.heap[leftchild]:  # to check whether the left child is smaller than the parent node, if it is smaller we are storing left child value in temp
            temp = leftchild
            
        if rightchild<len(self.heap) and self.heap[temp]>self.heap[rightchild]:  ## to check whether the right child is smaller than the parent node, if it is smaller we are storing right child value in temp
            temp = rightchild
            
        if temp == index:
            return
        
        self.heap[temp],self.heap[index] = self.heap[index],self.heap[temp]  # we are swapping the values
        self.bubbledown(temp)
        
    def insert(self,key):
        self.heap.append(key)  #appending the values in the list
        self.bubbleup(len(self.heap)-1)  #we are bubbling up 
        
    def extractmin(self):
        self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]  # we are swapping the minimum value to the last index
        temp = self.heap.pop()  #we are storing the min val in temp and we are removing it from the list
        self.bubbledown(0)  #after swapping we are doing bubbledown operation
        return temp  # we are returning the minimum value stored in temp
    
    def size(self):
        return len(self.heap)  # we are returning the size of the heap 
    
    
h = minheap()
h.insert(5);
h.insert(3);
h.insert(17);
h.insert(11);
h.insert(79);
h.insert(19);
h.insert(6);
h.insert(25);
h.insert(9);
print(h.heap)
print(h.getmin())
for i in range(len(h.heap)):
    print(h.extractmin())
    
        
            
        
        
        
            
        
        
    
        

