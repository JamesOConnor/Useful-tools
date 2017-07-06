import skimage.util as noi
import cv2
import numpy as np
import numpy.ma as ma
import sys

infile=sys.argv[1]
snr=float(sys.argv[2])

x=cv2.imread(infile).astype(float)

x=ma.masked_less(x,1)

updawg=ma.max(x)

x = x / ma.max(x);

v = ma.var(x) / (10**(snr/10));
if snr==0:
	v=0.00000001
x_noise=(noi.random_noise(x, mode='gaussian', mean=0, var=v)*updawg).astype(np.uint8)
if snr==0:
	cv2.imwrite('%s'%(infile.replace('.png', '_snr%s.png'%(snr))), x_noise)
elif '.jpg' in infile:
	cv2.imwrite('%s'%(infile.replace('.jpg', '_snr%s.jpg'%(snr))), x_noise)
elif '.png' in infile:
	cv2.imwrite('%s'%(infile.replace('.png', '_snr%s.tif'%(snr))), x_noise)
elif '.tif' in infile:
	cv2.imwrite('%s'%(infile.replace('.tif', '_snr%s.tif'%(snr))), x_noise)
