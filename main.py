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

def triangulations(n,pr=False):
    def trilist(L): #L is a list of vertices which we will triangulate.
        if len(L)==3: #If it's a triangle, there is one trivial triangulation.
            yield []
        else: #We now consider all possible positionings of the final line segment v0-vn-1
            for l in range(2,len(L)-2):
                new_edges=[(L[0],L[l]),(L[l],L[-1])]
                #Suppose we split the polygon at position l. Then we take
                #all the triangulations of both the left side and the right side.
                for edgelist1 in trilist(L[:l+1]):
                    for edgelist2 in trilist(L[l:]):
                        yield new_edges+edgelist2+edgelist1
            #The two other possibiliites involve v0-vn-1 being an ear.
            new_edges=[(L[1],L[-1])]
            for edgelist in trilist(L[1:]):
                yield new_edges+edgelist
            new_edges=[(L[0],L[-2])]
            for edgelist in trilist(L[:-1]):
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
N=0
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
    print("FOUND triangulations on n={} vertices:".format(N),triangulations(N,pr))
else:
    print()
    print("CALCULATED triangulations on n={} vertices:".format(N),tricounter(N))
