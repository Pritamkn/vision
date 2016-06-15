def give_extpoints(f):
	'''
	inputs:
		f: contour
	output:
		coordinates of extreme points
	'''
	fl=tuple(f[f[:,:,0].argmin()][0])
	fr=tuple(f[f[:,:,0].argmax()][0])


	ft=tuple(f[f[:,:,1].argmin()][0])
	fb=tuple(f[f[:,:,1].argmax()][0])

	return {"top":ft,"left":fl,"right":fr,"bottom":fb}
