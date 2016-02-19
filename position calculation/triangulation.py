from globalVariables import estimotePosition
from numpy.linalg import norm
from math import pow, sqrt
from numpy import cross, dot, array
def triangulation(estimoteSortDist):
	Dist = [item[1] for item in estimoteSortDist]
	maclist = [item[0] for item in estimoteSortDist]
	P1 = array(estimotePosition[maclist[0]])
	P2 = array(estimotePosition[maclist[1]])
	P3 = array(estimotePosition[maclist[2]])
	ex = (P2 - P1)/(norm(P2 - P1))
	i = dot(ex, P3 - P1)
	ey = (P3 - P1 - i*ex)/(norm(P3 - P1 - i*ex))
	ez = cross(ex,ey)
	d = norm(P2 - P1)
	j = dot(ey, P3 - P1) 
	x = (pow(Dist[0],2) - pow(Dist[1],2) + pow(d,2))/(2*d)
	y = ((pow(Dist[0],2) - pow(Dist[2],2) + pow(i,2) + pow(j,2))/(2*j)) - ((i/j)*x)
	m = pow(Dist[0],2) - pow(x,2) - pow(y,2)
	if m < 0:
		z = sqrt(-m)
	else:
		z = sqrt(m)
	triPt = P1 + x*ex + y*ey + z*ez
	return triPt