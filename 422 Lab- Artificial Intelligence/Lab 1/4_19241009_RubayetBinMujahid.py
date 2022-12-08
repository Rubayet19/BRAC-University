#task1

global count
def maxRegion (region, i, j):
    global count
    count += 1

    region[i][j] = 'N'

    direction = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

    for v in direction:

        if (i + v[0]) >= 0 and (i + v[0]) < len(region) and (j + v[1]) >= 0 and (j + v[1]) < len(region[0]) and \
                region[i + v[0]][j + v[1]] == 'Y':
            maxRegion(region, i + v[0], j + v[1])


file = open("input.txt", "r")
region = []
for line in file.readlines():
    region.append([x for x in line.rstrip('\n').split(' ')])

ans = 0

for i in range(0, len(region)):
    for j in range(0, len(region[0])):

        if region[i][j] == 'Y':

            global count
            count = 0

            maxRegion(region, i, j)

            if count > ans:
                ans = count

print(ans)


#task 2

from queue import Queue

def isSafe(new_r,new_c,R,C):
    return (new_r>=0 and new_c>=0 and new_r<R and new_c<C)

def getMinTime(mat,R,C):
    alien=Queue()
    visited=[[0 for i in range(C)] for j in range(R)]
    #print(visited)

    no_of_human=0
    min_time=-1

    for i in range(R):
        for j in range(C):
            if(mat[i][j]=='A'):
                alien.put((i,j))
                visited[i][j]=1
            elif(mat[i][j]=='H'):
                no_of_human+=1

    r=[-1,0,0,1]
    c=[0,-1,1,0]

    while not alien.empty():
        current_no_of_alien=alien.qsize()
        while current_no_of_alien!=0:
            k,l=alien.queue[0]
            alien.get()
            if(mat[k][l]=='H'):
                no_of_human-=1
            for i in range(4):
                new_r=k+r[i]
                new_c=l+c[i]

                if(isSafe(new_r,new_c,R,C) and visited[new_r][new_c]==0 and mat[new_r][new_c]=='H'):
                    alien.put((new_r,new_c))
                    visited[new_r][new_c]=1
            current_no_of_alien-=1

        min_time+=1

    print("Time:",min_time,"minutes")
    if(no_of_human==0):
        print("No one survived",end='')
    else:
        print(no_of_human,"survived")




R = int(input("Enter number of Rows "))
C = int(input("Enter number of Columns "))
mat=[]
for i in range(R):
 mat.append([j for j in input().split()])


getMinTime(mat,R,C)