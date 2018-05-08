import numpy, math
from rs import RoughSet
import copy

A = [
	[1 , 'y', 'y', 'nor', 'n'],
	[2 ,'y', 'y', 'hi', 'y'],
	[3 ,'y', 'y', 'vhi', 'y'],
	[4 ,'n', 'y', 'nor', 'n'],
	[5 ,'n', 'n', 'hi', 'n'],
	[6 ,'n', 'y', 'vhi', 'y']
	]
A1 = [
	[1 ,'1', '1', '0', '0'],
	[2 ,'1', '1', '1', '1'],
	[3 ,'1', '1', '2', '1'],
	[4 ,'0', '1', '0', '0'],
	[5 ,'0', '0', '1', '0'],
	[6 ,'0', '1', '2', '1'],
	[7 ,'0', '0', '?', '1'],
	[8 ,'0', '1', '2', '0']
	]
A1 = numpy.array(A1)

A = numpy.array(A)


class DataImputation(object):


	def __init__(self, A, missing=None, p=2, s=None, fn="sum"):
		self.fn = fn
		self.p = p
		self.missing_val = '?'
		if missing is None:
			self.A, self.missing = self.separate(A)
		else:
			self.A = numpy.array(A)
			self.missing = numpy.array(missing)
		if s == 'ig1':
			self.s = self.calc_IG1()
		elif s == 'ig2':
			self.s = self.calc_IG2()
		elif s == 'rs_ig':
			self.s = self.calc_roughset_ig()
		else:
			self.s = numpy.ones(self.A.shape[1])
		



	def separate(self, A):
		nA = []
		missing = []
		for row in A:
			if len(row[row=='?']) > 0:
				missing.append(row)
			else:
				nA.append(row)
		return numpy.array(nA), numpy.array(missing)



	def imputate(self, row):
		row = numpy.array(row)
		missing = numpy.where(row == self.missing_val)[0]
		selected = range(len(row))
		selected = numpy.delete(selected, missing)
		min_dist = 100000000000.0
		mini = 0
		for ri, row2 in enumerate(self.A):
			dist = self.distance(row[selected], row2[selected])
			if dist < min_dist:
				min_dist = dist
				mini = ri

		nrow = copy.deepcopy(row)
		nrow[nrow=='?'] = self.A[mini, nrow=='?']
		return nrow
		


	def distance(self, row1, row2):
		return self.ps_distance(row1, row2, self.p, self.s, self.fn)



	def ps_distance(self, row1, row2, p, s, fn="sum"):
		dist = []
		for i in range(len(row1)):
			val1 = float(row1[i])
			val2 = float(row2[i])
			dd = (abs(1.0*val1**p - val2**p)) / (self.s[i]+ 0.00001)
			d = math.pow(dd, 1.0/p)
			dist.append(d)
		if fn == "sum":
			return sum(dist)
		if fn == "min":
			return min(dist)
		if fn == "max":
			return max(dist)
		if fn == "avg":
			return sum(dist) * 1.0 / len(dist)
		return sum(dist)



	def abs_distance(self, row1, row2):
		return self.ps_distance(row1, row2, 1, numpy.ones(self.A.shape[1]))



	def euc_distance(self, row1, row2):
		return self.ps_distance(row1, row2, 2, numpy.ones(self.A.shape[1]))



	def imputate_all(self):
		for mrow in range(len(self.missing)):
			self.missing[mrow] = self.imputate(self.missing[mrow])
			


	def calc_IG1(self):
		ig1 = []
		for col in self.A.T:
			col_set=set(col)
			col_ig = 0.0
			for val in col_set:
				n_val = len(col[col==val])
				prop = 1.0*n_val/len(col)
				col_ig += -1.0 * prop * math.log(prop, 2)
			ig1.append(col_ig)
		for ig in range(len(ig1) - 1):
			ig1[ig] = abs(ig1[-1] - ig1[ig])
		return ig1


	def calc_IG2(self):
		n = self.A.shape[0] * 1.0
		#print self.A
		infoD = 0
		domainD = set(self.A[:, -1])
		infoiD = [0.0 for __ in range(self.A.shape[1]-1)]
		for v in domainD: 
			nv = 1.0 * len(self.A[:, -1][self.A[:, -1] == v])
			infoD -= nv / n * math.log(nv / n, 2)
		#print infoD
		for i in range(self.A.shape[1] - 1):
			domaini = set(self.A[:, i])
			#iD = [[[] for __ in domainD] for _ in domaini]
			iD = dict([(ii, dict([(di, 0) for di in domainD])) for ii in domaini])
			infoi = 0.
			for ii in domaini:
				sumi = 0.
				dinfo = 0.
				for di in domainD:
					temp = self.A[:, i][self.A[:, -1]== di]
					iD[ii][di] = len(temp[temp == ii]) * 1.0
				sumi = sum(iD[ii].values())
				for di in iD[ii]:
					#print ii, di, sumi , iD[ii][di], n
					if iD[ii][di] != 0:
						dinfo -= iD[ii][di] / n * math.log(iD[ii][di] / n, 2)
						#print iD[ii][di] , n , dinfo
				dinfo *= (sumi / n)
				infoi += dinfo
			#print iD
			#print infoi, "\n-----------------------------"
				#print infoi
			infoiD[i] = infoD - infoi
			#print iD 
			#print infoiD
		return infoiD




	def calc_roughset_ig(self):
		
		rs = RoughSet(self.A[:,:-1] , self.A[:, 1])
		rs_ig = rs.get_loss()
		#print rs_ig
		return numpy.ones(len(rs_ig)) - rs_ig


	def mean_squared_error(self, truth):
		evgs = []
		for i in range(self.missing.shape[0]):
			es = []
			for j in range(self.missing.shape[1]):
				e = float(self.missing[i][j]) - float(truth[i][j])
				es.append(e**2)
			evg = numpy.mean(es)
			evgs.append(evg)
		return numpy.mean(evgs)


	def root_mean_squared_error(self, truth):
		return math.pow(self.mean_squared_error(truth), 0.5)

	def mean_absolute_error(self, truth):
		evgs = []
		for i in range(self.missing.shape[0]):
			es = []
			for j in range(self.missing.shape[1]):
				e = float(self.missing[i][j]) - float(truth[i][j])
				es.append(abs(e))
			evg = numpy.mean(es)
			evgs.append(evg)
		return numpy.mean(evgs)

if __name__ == '__main__':
	di = DataImputation(A1[:, 1:], 1, 'ig1')
	#di.imputate_all()
	print di.calc_roughset_ig()