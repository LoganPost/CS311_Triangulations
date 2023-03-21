def tricounter(n):
    arr=[0 for i in range(n+1)]
    arr[3]=1
    def tric(m):
        nonlocal arr
        if arr[m]:
            return arr[m]
        else:
            count=0
            for l in range(2,m-2):
                count+=tric(l+1)*tric(m-l)
            count+=2*tric(m-1)
            arr[m]=count
            return count
    for m in range(4,n):
        tric(m)
    return tric(n)

def triangulations_old(n,pr=False):
    def trilist(V): #L is a list of vertices which we will triangulate.
        if len(V)==3: #If it's a triangle, there is one trivial triangulation.
            yield []
        else: #We now consider all possible positionings of the final line segment v0-vn-1
            for l in range(2,len(V)-2):
                new_edges=[(V[0],V[l]),(V[l],V[-1])]
                #Suppose we split the polygon at position l. Then we take
                #all the triangulations of both the left side and the right side.
                for edgelist1 in trilist(V[:l+1]):
                    for edgelist2 in trilist(V[l:]):
                        yield new_edges+edgelist2+edgelist1
            #The two other possibiliites involve v0-vn-1 being an ear edge.
            new_edges=[(V[1],V[-1])]
            for edgelist in trilist(V[1:]):
                yield new_edges+edgelist
            new_edges=[(V[0],V[-2])]
            for edgelist in trilist(V[:-1]):
                yield new_edges+edgelist
    #We now use this generator to count (and print) all the traingulations
    count=0
    perc = tricounter(n) // 100
    # Master_Set=set()
    for i in trilist(list(range(n))):
        if pr:
            print(i)
        count+=1
        # Master_Set.add(i)
        if n>15 and not pr:
            if count%perc==0:
                print("{}%".format(count//perc),end=" ")
                if count%(perc*20)==0:
                    print()
    return count

def triangulations(n,pr=False):
    def trilist(bot,top): #L is a list of vertices which we will triangulate.
        if top-bot==2: #If it's a triangle, there is one trivial triangulation.
            yield []
        else: #We now consider all possible positionings of the final line segment v0-vn-1
            for splt in range(bot+2,top-1):
                new_edges=[(bot,splt),(splt,top)]
                #Suppose we split the polygon at position splt. Then we take
                #all the triangulations of both the left side and the right side.
                for edgelist1 in trilist(bot,splt):
                    edgelist1.extend(new_edges)
                    for edgelist2 in trilist(splt,top):
                        edgelist2.extend(edgelist1)
                        yield edgelist2
            #The two other possibiliites involve v0-vn-1 being an ear edge.
            for edgelist in trilist(bot,top-1):
                edgelist.append((bot,top-1))
                yield edgelist
            for edgelist in trilist(bot+1,top):
                edgelist.append((bot+1,top))
                yield edgelist
    #We now use this generator to count (and print) all the traingulations
    count=0
    perc = tricounter(n) // 100
    # Master_Set=set()
    for tri in trilist(0,n-1):
        if pr:
            tri.sort(key=lambda k: k[0])
            print(tri)
        count+=1
        # Master_Set.add(i)
        if n>15 and not pr:
            if count%perc==0:
                print("{}%".format(count//perc),end=" ")
                if count%(perc*20)==0:
                    print()
    return count

N=0
from time import time
try: N=int(input("How many vertices in the polygon? Enter a number: "))
except: pass
while N<3 or N>100000:
    print("Input error, try again.")
    N = int(input("How many vertices in your polygon? Enter a number: "))

print()
if N>25:
    print("That is likely too many to find them all. I recommend only calculating.")

want_to_find=input("Finding triangulations is slow, but calculating is fast. Would you like to FIND all triangulations? Y for yes, N for no: ") in ("y","Y","yes","Yes")

if want_to_find:
    pr=input("PRINT all triangulations? Y for yes, N for no: ") in ("y","Y","yes","Yes","p","P","print","Print")
    print()
    t=time()
    print("FOUND triangulations on n={} vertices:".format(N),triangulations(N,pr))
    print("Time: ",time()-t,"seconds.")
else:
    print()
    print("CALCULATED triangulations on n={} vertices:".format(N),tricounter(N))
