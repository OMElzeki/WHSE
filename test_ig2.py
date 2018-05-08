import numpy
from missing import DataImputation


A1 = [
	["30", "h", "n", "b", "n"],
	["30", "h", "n", "g", "n"],
	["3140", "h", "n", "b", "y"],
	["40", "m", "n", "b", "y"],
	["40", "l", "y", "b", "y"],
	["40", "l", "y", "g", "n"],
	["3140", "l", "y", "g", "y"],
	["30", "m", "n", "b", "n"],
	["30", "l", "y", "b", "y"],
	["40", "m", "y", "b", "y"],
	["30", "m", "y", "g", "y"],
	["3140", "m", "n", "g", "y"],
	["3140", "h", "y", "b", "y"],
	["40", "m", "n", "g", "n"],
	
	]
A1 = numpy.array(A1)
di = DataImputation(A1, [], p=1)
	#di.imputate_all()
print di.calc_IG2()