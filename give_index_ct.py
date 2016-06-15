import numpy as np
def give_index_ct(contour,height):
	'''
	input:
		contour:
	output:
		indices of points on the contour at a given height
	'''
	x=[]
	for i in range(0,len(contour)-2):
		if i%2==0:
			continue
		a=contour[i,0,1]-height
		b=contour[i+2,0,1]-height
		if a == 0:
			x.append(i)
		elif a*b<0:
			#print i,contour[i],'\n',i+2,contour[i+2]
			x.append(i+1)
	return x
