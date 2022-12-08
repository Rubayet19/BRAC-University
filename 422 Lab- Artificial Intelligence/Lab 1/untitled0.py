
global count

def maxRegion(area,i,j):
    global count
    count+=1 

    area[i][j]='N'

    direction=[[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

    for elem in direction:

        if (i+elem[0])>=0 and (i+elem[0])<len(area) and (j+elem[1])>=0 and (j+elem[1])<len(area[0]) and area[i+elem[0]][j+elem[1]]=='Y':

            maxRegion(area,i+elem[0],j+elem[1])
    
    


file=open("input.txt","r")
area=[]
for line in file.readlines():
    area.append( [ x for x in line.rstrip('\n').split(' ') ] )

result=0

for i in range(0,len(area)):
    for j in range(0,len(area[0])):
       
        if area[i][j]=='Y':
            
            global count 
            count=0
            
            maxRegion(area,i,j)

            if count>result:
                result=count

print(result)

