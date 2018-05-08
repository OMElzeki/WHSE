import csv, numpy, copy, random
from missing import DataImputation


data_file='/media/attia42/Data2/workspace/projects/missing_value/data/forestfires.csv'
data = []
with open(data_file, 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		data.append(row)

data = numpy.array(data)
data = data[:, [0,1,4,5,6,7,8,9,10,11,12]]
#data = data.astype(float)


#make missing 
A = []
missing = []
missing_label = []
data_w_missing = copy.deepcopy(data)
for row in data:
	if random.random() > 0.7:
		cp1 = copy.deepcopy(row)
		cp1[random.randint(0, len(row) - 1)] = '?'
		missing.append(cp1)
		missing_label.append(row)
	else:
		A.append(row)


#di = DataImputation(A, missing)
#di.imputate_all()

#for i, row in enumerate(di.missing):
	#print row
	#print missing_label[i]
	#print '--------------------------------------------------------------------------'

#print di.mean_squared_error(missing_label)

print "p = 1, s = 1"
di = DataImputation(A, missing, p=1)
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'

print "p = 1, s = Information Gain1"
di = DataImputation(A, missing, p=1, s='ig1')
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'

print "p = 1, s = Information Gain2"
di = DataImputation(A, missing, p=1, s='ig2')
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'





print "p = 1, s = Roughset Info gain"
di = DataImputation(A, missing, p=1, s='rs_ig')
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'


print "p = 2, s = 1"
di = DataImputation(A, missing, p=2)
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'

print "p = 2, s = Information Gain1"
di = DataImputation(A, missing, p=2, s='ig1')
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'

print "p = 2, s = Roughset Info gain"
di = DataImputation(A, missing, p=2, s='rs_ig')
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'

print "p = 3, s = 1"
di = DataImputation(A, missing, p=3)
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'

print "p = 3, s = Information Gain1"
di = DataImputation(A, missing, p=3, s='ig1')
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'


print "p = 3, s = Roughset Info gain"
di = DataImputation(A, missing, p=3, s='rs_ig')
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)













print "p = 1, s = 1, fn=max"
di = DataImputation(A, missing, p=1, fn="max")
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'

print "p = 1, s = Information Gain1, fn=max"
di = DataImputation(A, missing, p=1, s='ig1', fn="max")
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'

print "p = 1, s = Information Gain2, fn=max"
di = DataImputation(A, missing, p=1, s='ig2', fn="max")
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'





print "p = 1, s = Roughset Info gain, fn=max"
di = DataImputation(A, missing, p=1, s='rs_ig', fn="max")
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'


print "p = 2, s = 1, fn=max"
di = DataImputation(A, missing, p=2, fn="max")
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'

print "p = 2, s = Information Gain1, fn=max"
di = DataImputation(A, missing, p=2, s='ig1', fn="max")
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'

print "p = 2, s = Roughset Info gain, fn=max"
di = DataImputation(A, missing, p=2, s='rs_ig', fn="max")
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'

print "p = 3, s = 1, fn=max"
di = DataImputation(A, missing, p=3, fn="max")
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'

print "p = 3, s = Information Gain1, fn=max"
di = DataImputation(A, missing, p=3, s='ig1', fn="max")
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
print '--------------------------------------------------------------------------'


print "p = 3, s = Roughset Info gain, fn=max"
di = DataImputation(A, missing, p=3, s='rs_ig', fn="max")
di.imputate_all()
print "mean_squared_error: ", di.mean_squared_error(missing_label)
print "root_mean_squared_error: ", di.root_mean_squared_error(missing_label)
print "mean_absolute_error: ", di.mean_absolute_error(missing_label)
