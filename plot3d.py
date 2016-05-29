from outer import encContour
import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def plot3dHuman (front,side):
	f=encContour(front)
	s=encContour(side)
	def retval (t,f) :
		x=[]
		for i in range(0,len(f)-1):
			a=f[:,1][i]-t
			b=f[:,1][i+1]-t
			if a*b == 0 :
				if a==0:
					x.append(f[:,0][i])
				else:
					x.append(f[:,0][i+1])
			else:
				if a*b<0:
					x.append((f[:,0][i]+f[:,0][i+1])/2)
		sorted(x)
		y=[]
		for i in range(0,len(x)-1):
			if x[i] == x[i+1] :
				continue
			y.append(x[i])
		if len(x) is not 0 :
			y.append(x[-1])
		return y


	fl=tuple(f[f[:,:,0].argmin()][0])
	fr=tuple(f[f[:,:,0].argmax()][0])
	 
	sl=tuple(s[s[:,:,0].argmin()][0])
	sr=tuple(s[s[:,:,0].argmax()][0])

	ft=tuple(f[f[:,:,1].argmin()][0])
	fb=tuple(f[f[:,:,1].argmax()][0])

	st=tuple(s[s[:,:,1].argmin()][0])
	sb=tuple(s[s[:,:,1].argmax()][0])
	#from height import height
	#height('man_front.jpg')
	#print ft,fb
	#print st,sb
	f1=f
	f1=f1[:,0]-[fr[0]-(fl[0]+fr[0])/2,fb[1]]
	f1[:,1]=-f1[:,1]
	s1=s
	s1=s1[:,0]-[sl[0]+(sl[0]+sr[0])/2,sb[1]]
	s1[:,1]=-s1[:,1]
	matplotlib.rcParams['legend.fontsize']=10
	fig=plt.figure()
	ax=fig.gca(projection='3d')
	s1
	y=np.zeros(len(f1[:,0]),dtype=np.int64)
	#ax.plot(f1[:,0],y,f1[:,1],label='front')

	x=np.zeros(len(s1[:,0]),dtype=np.int64)
	#ax.plot(x,s1[:,0],s1[:,1],label='side')
	ax.set_aspect('equal')
	#print retval(800,f1)
	theta=np.linspace(0,2*np.pi,40)
	max(max(f1[:,1]),max(s1[:,1]))
	iterator=np.linspace(1,max(max(f1[:,1]),max(s1[:,1])),120)
	X=[] ;Y=[];Z=[]
	for fl in iterator:
		x1=retval(fl,f1)
		y1=retval(fl,s1)
		if len(x1) in [0,1,3,5] :
			continue
		if len(x1) == 6:
			x_a=(x1[0]+x1[1])/2
			y_a=(y1[0]+y1[1])/2
			x_a1=(x1[4]+x1[5])/2
			a=(x1[1]-x1[0])/2
			a1=(x1[5]-x1[4])/2
			b=a
			b1=a1
			for temp in (x1[0]+x1[1])/2+a*np.cos(theta) :
				X.append(temp)
			for temp in (y1[0]+y1[1])/2+b*np.sin(theta) :
				Y.append(temp)
				Z.append(fl)
			for temp in (x1[4]+x1[5])/2+a1*np.cos(theta) :
				X.append(temp)
			for temp in (y1[0]+y1[1])/2+b1*np.sin(theta) :
				Y.append(temp)
				Z.append(fl)
		xf=[]
		if len(x1) == 6 :
			xf=[x1[2],x1[3]]
		else :
			xf=x1
	#	print len(x1),len(y1)
		x_a=(xf[1]+xf[0])/2
		y_a=(y1[0]+y1[1])/2
		a=(xf[1]-xf[0])/2
		b=(y1[1]-y1[0])/2
		#print y1,b
		for temp in x_a+a*np.cos(theta) :
			X.append(temp)
		for temp in y_a+b*np.sin(theta) :
			Y.append(temp)
			Z.append(fl)
		
		if(len(x1)==4):
			a=(x1[3]-x1[2])/2
			x_a=(x1[3]+x1[2])/2
			y_a=(y1[0]+y1[1])/2
			for temp in x_a+a*np.cos(theta) :
				X.append(temp)
			for temp in y_a+b*np.sin(theta) :
				Y.append(temp)
				Z.append(fl)
	fig=plt.figure()
	ax=fig.add_subplot(111,projection='3d')
	#print len(X),len(Y),len(Z)
	ax.plot_wireframe(X,Y,Z,rstride=10,cstride=10)
	# Create cubic bounding box to simulate equal aspect ratio
	max_range = np.array([max(X)-min(X), max(Y)-min(Y),max(Z)-min(Z)]).max()
	Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(max(X)+min(X))
	Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(max(Y)+min(Y))
	Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(max(Z)+min(Z))
	# Comment or uncomment following both lines to test the fake bounding box:
	for xb, yb, zb in zip(Xb, Yb, Zb):
	   ax.plot([xb], [yb], [zb], 'w')
	plt.show()

	#print "height_front :  ",ft[0]-fb[0], "|||", ft[1]-fb[1]
	#print "height_side  :  ",st[0]-sb[0] ,"|||" ,st[1]-sb[1]
