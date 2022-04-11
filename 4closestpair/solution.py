import math
from operator import attrgetter
import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(P1, P2):
    return math.dist((P1.x, P2.x), (P1.y, P2.y))

def min_among_three(P1, P2, P3):
    dist1 = math.dist((P1.x, P2.x), (P1.y, P2.y))
    dist2 = math.dist((P1.x, P3.x), (P1.y, P3.y))
    dist3 = math.dist((P2.x, P3.x), (P2.y, P3.y))
    return min(dist1, dist2, dist3)
    

def main():
    lines_raw = sys.stdin.readlines()
    first_line =  lines_raw[0].strip().split()
    nbr_points = int(first_line[0])
    Px = list()
    Py = list()
    for k in range(1, nbr_points+1):
        x = int(lines_raw[k].strip().split()[0])
        y = int(lines_raw[k].strip().split()[1])

        p = Point(x,y)  
        Px.append(p)
        Py.append(p)

    Px = list(sorted(Px, key=attrgetter('x')))
    Py = list(sorted(Px, key=attrgetter('y')))

    print('%.6f' % closest_pair(Px,Py))

# Px points sorted by x, Py points sorted by y
def closest_pair(Px, Py):

    n = len(Px)
    if (n==2):
        return dist(Px[0], Px[1])
    if (n==3):
        return min_among_three(Px[0], Px[1], Px[2])

    ## Divide
    mid = Px[int(n/2)]
    index = int(n/2)

    dl = closest_pair(Px[0:index], Py)
    dr = closest_pair(Px[index:n], Py)
    d = min(dl,dr)

    # Set with points in Py where x is in range mid-delta, mid+delta
    S = list()
    for point in Py:
        if mid.x-d<point.x<mid.x+d:
            S.append(point)

    for point_index in range(0,len(S)):
        if S[point_index].x<mid.x:

            for i in range(point_index+1,n): #Go up
                if(S[i].y>S[point_index].y+d):
                    break
                deltaD = dist(S[point_index],S[i])
                d = min(d,deltaD)
            for i in range(int(n/2)-1,0,-1): #Go down
                if(S[i].y<point.y+d):
                    break
                deltaD = dist(point,S[i])
                d = min(d,deltaD)
    return d
    """ 
    S = list()
    for p in Py:
        if  mid.x-d < p.x < mid.x+d :
            S.append(p)
    print(S)
    for i in range(len(S)):
        for j in range(1):
            d = min(d, (dist(S[i], S[i+j])))
    return d
    """
main()


