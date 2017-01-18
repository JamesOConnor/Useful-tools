import cv2
import numpy as np
import sys
import seaborn as sns

im = sys.argv[1]
im = cv2.imread(im)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(float)
rows,cols = gray.shape

rows_diff = np.zeros_like(gray)
cols_diff = np.zeros_like(gray)
for r in range(rows):
	if r == 0:
		continue
	rows_diff[r,:] = gray[r,:] - gray[r-1,:]
for c in range(cols):
	if c == 0:
		continue
	cols_diff[:,c] = gray[:,c] - gray[:,c-1]

y,binEdges=np.histogram(rows_diff,bins=40, range=(-20,20))
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
sns.plt.plot(bincenters, y, '-', label='Rows: Proportion -5 > x < 5 = %s%%' % np.round(100*(y[15:25].sum()/float(gray.size)), decimals = 2))
sns.plt.title('Distribution of gradients in image rows (Y direction)')

y,binEdges=np.histogram(cols_diff,bins=40, range=(-20,20))
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
sns.plt.plot(bincenters, y, '-', label='Cols: Proportion -5 > x < 5 = %s%%' % np.round(100*(y[15:25].sum()/float(gray.size)), decimals = 2))
sns.plt.title('Distribution of gradients in image cols (X direction)')
sns.plt.ylabel('Pixel count')
sns.plt.xlabel('Change from neighbouring pixel value')
sns.plt.legend()
sns.plt.savefig('Image_gradients.png')
sns.plt.clf()
