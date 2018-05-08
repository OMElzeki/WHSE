

def Abs_Diff_Distance
	sum_dist = 0
	for i in range(len(row1)):
		val1 = int(row1[i])
		val2 = int(row2[i])
		sum_dist += abs(val1 - val2)
	return sum_dist


