# make_set
n=12
xparent = [-1]*n
xrank = [0]*n

def findSet(i):
    if xparent[i]==-1:
        return i
    xparent[i] = findSet(xparent[i])
    return xparent[i]

def unionSet(i,j):
    iroot = findSet(i)
    jroot = findSet(j)
    if xrank[iroot] > xrank[jroot]:
        xparent[jroot] = iroot
    elif xrank[iroot] < xrank[jroot]:
        xparent[iroot] = jroot
    else:
        xparent[jroot] = iroot
        xrank[iroot]+=1

unionSet(5,8)
unionSet(5,2)
unionSet(5,4)
unionSet(4,6)

print(xparent)
print(xrank)