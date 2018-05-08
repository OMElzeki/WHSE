import numpy

D1 = ['n', 'y', 'y', 'n', 'n', 'y']
D2 = ['0', '1', '1', '0', '0', '1', '1', '0']

D2= numpy.array(D2)

A1 = [
	[1 , 'y', 'y', 'nor'],
	[2 ,'y', 'y', 'hi'],
	[3 ,'y', 'y', 'vhi'],
	[4 ,'n', 'y', 'nor'],
	[5 ,'n', 'n', 'hi'],
	[6 ,'n', 'y', 'vhi']
	]
A2 = [
	[1 ,'1', '1', '0'],
	[2 ,'1', '1', '1'],
	[3 ,'1', '1', '2'],
	[4 ,'0', '1', '0'],
	[5 ,'0', '0', '1'],
	[6 ,'0', '1', '2'],
	[7 ,'0', '0', '1'],
	[8 ,'0', '1', '2']
	]
A2 = numpy.array(A2)

class RoughSet(object):
	def __init__(self, A, D=None):
		#print A.shape
		#print D.shape
		A = numpy.array(A)
		if D == None:
			self.A = A[:, :-1]
			self.D = A[-1]
		else:
			self.A = A
			self.D = numpy.array(D)
	def IND(self, A):
		#print A.shape
		if len(A.shape) > 1:
			inds = numpy.lexsort([A[:,i] for i in range(A.shape[1])])
		else:
			inds = numpy.argsort(A)
		#print A[inds]
		sets = []
		current = []
		#print inds
		for i, ind in enumerate(inds):
			current.append(ind + 1)
			
			def compare():
				eq = True
				if len(A.shape) > 1:
					eq = (A[ind] != A[inds[i+1]]).any()
				else:
					eq = A[ind] != A[inds[i+1]]
				return eq
			if i+1 >= len(inds) or compare():
				sets.append(set(current))
				current = []
		return sets


	

	def get_xlower(self, A, indD):
		ABind = self.IND(A)
		X_lower = []
		for e in ABind:
			for De in indD:
				if De >= e:
					X_lower.append(e)
					break
		#print "xl ", X_lower
		return X_lower
	def get_delta(self, A, indD):
		X_lower = self.get_xlower(A, indD)
		l_lower = 0.0
		for xl in X_lower:
			l_lower += len(xl)
		delt_c = 1.0*l_lower / A.shape[0]
		#print delt_c
		return delt_c


	def get_loss(self):
		indD = self.IND(self.D)
		delta_D = self.get_delta(self.A, indD)
		#print delta_D
		#print indD
		losses = []
		for att in range(0,self.A.shape[1]):

			selected = range(0, self.A.shape[1])
			selected.remove(att)
			
			
			delt_c = self.get_delta(self.A[:, selected], indD)
			gama_c = delta_D - delt_c
			losses.append(gama_c)
			#print losses
		return losses



if __name__ == '__main__':
	rs = RoughSet(A2[:, 1:], D2)
	print rs.get_loss()