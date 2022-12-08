
def recsel(n,index=0):
    if index==len(n):
        return -1
    min=index  
    for j in range(index+1,len(n)):
        if n[j]<n[min]:
            min=j
    temp=n[index]
    n[index]=n[min]
    n[min]=temp
    return recsel(n,index+1)
    
lst=[5,2,8,9,3,1,0,7]
recsel(lst)
for i in lst:
    print(i, end = ' ')


    