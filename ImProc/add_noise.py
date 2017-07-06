import skimage.util as noi
import cv2
import numpy as np
import numpy.ma as ma
import sys

def add_noise(infile, snr):
    '''
    :param infile: file to process
    :param snr: SNR, in decibels, which the output image contains vs input
    :return: File written to disc
    '''
    x = cv2.imread(infile).astype(float)
    x = ma.masked_less(x, 1)  # zeros give error
    uplim = ma.max(x)
    x = x / uplim
    v = ma.var(x) / (10 ** (snr / 10));
    if snr == 0:
        v = 0.00000001
    x_noise = (noi.random_noise(x, mode='gaussian', mean=0, var=v) * uplim).astype(np.uint8)
    if snr == 0:
        cv2.imwrite('%s' % (infile.replace('.png', '_snr%s.png' % (snr))), x_noise)
    elif '.jpg' in infile:
        cv2.imwrite('%s' % (infile.replace('.jpg', '_snr%s.jpg' % (snr))), x_noise)
    elif '.png' in infile:
        cv2.imwrite('%s' % (infile.replace('.png', '_snr%s.tif' % (snr))), x_noise)
    elif '.tif' in infile:
        cv2.imwrite('%s' % (infile.replace('.tif', '_snr%s.tif' % (snr))), x_noise)

if __name__ == '__main__':
    infile = sys.argv[1]
    snr = float(sys.argv[2])
    add_noise(infile, snr)

