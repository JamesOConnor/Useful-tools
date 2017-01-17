import glob
import sys
import numpy as np

def make_image_pair_file():
	num = int(sys.argv[1])
	fns = glob.glob('*.%s'%(str(sys.argv[2])))
	opt = str(sys.argv[3])
	delimiter = str(sys.argv[4])

	final = []
	final_fmt = []

	if delimiter=='space':
		delim = ' '
	elif delimiter=='comma':
		delim = ','

	if opt == 'linear':
		for n,i in enumerate(fns):
			li = []
			for fn in fns[n+1:n+num+1]:
				li.append([i, fn])
			final.extend(li)
		if delim==' ':
			for i in final:
				final_fmt.append(i[0] + ' ' + i[1])
			np.savetxt('list.txt', final_fmt, fmt='%s')
		else:
			np.savetxt('list.txt', final, fmt='%s', delimiter=',')


	elif opt == 'circular':
		procced_files=[]
		final=[]
		for n,i in enumerate(fns):
			li = []
			if n < num:
				for n,fn in enumerate(np.concatenate((fns[-num+n:], fns[:n+num+1]), axis=0)):
					if fn in procced_files:
						continue
					if n == num:
						continue
					li.append([i, fn])
				procced_files.append(i)
			else:
				for fn in fns[n+1:n+num+1]:
					li.append([i, fn])
			final.extend(li)
		if delim==' ':
			for i in final:
				final_fmt.append(i[0] + ' ' + i[1])
			np.savetxt('list.txt', final_fmt, fmt='%s')
		else:
			np.savetxt('list.txt', final, fmt='%s',delimiter=',')
make_image_pair_file()
