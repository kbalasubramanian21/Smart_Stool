from globalVariables import txDict
from globalVariables import n
from operator import sorted
from numpy import mean
def positionCalc(estimoteDict):
	rssiDict = {key:mean(value) for (key,value) in estimoteDict.items()}
	estimoteDistance = {key:(10**((rssiDict[key]-txDict[key])/(10*n))) for key in rssiDict}
	estimoteSortDist = sorted(estimoteDistance.items(), key = operator.itemgetter(1))
	return estimoteSortDist[0:3]