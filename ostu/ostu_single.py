import skimage.io
import matplotlib.pyplot as plt
from oct2py import Oct2Py
import numpy as np

if __name__ == '__main__':
    pixels = skimage.io.imread("einstein.jpg").flatten("F") # Read the grey-level image

    # unique, counts = np.unique(pixels, return_counts=True)
    # d = dict(zip(unique, counts))

    # p = unique / len(pixels)

    # p = [pixels.count(pixel) for pixel in range(256)]

    hist, x = np.histogram(pixels, bins=256, range=(0, 255))
    p = hist / len(pixels) # Calculate the possibility

    # m = Oct2Py()

    # hn1 = m.load("/Users/pumpkin/Documents/MATLAB/Fall 2021/EECE 6357/otsu/hn1.mat")['hn1'][1:]
    # print(hn1)
    # print(p[2560])
    # print(p[2560])

    # u_T = sum([i * v for i, v in enumerate(p)])
    _range = np.array(range(1, len(p)+1))
    u_T = np.sum(p * _range)

    # sigma_k = np.zeros(256)
    # w_0 = 0
    # w_1 = 0
    # e_k = 0
    # for k in range(256):
    #     w_0 += p[k]
    #     w_1 += 1 - p[k]
    #     e_k += (k+1)*p[k]
    #     sigma_k[k] = (u_T * w_0 - e_k)**2 / (w_0 * w_1)

    w_0 = np.cumsum(p)
    w_1 = np.cumsum(1-p)
    e_k = np.cumsum(_range*p)
    
    np.seterr(divide='ignore', invalid='ignore')
    sigma_k = np.nan_to_num((u_T * w_0 - e_k)**2 / (w_0 * w_1), 0)
    argvalue, argmax = np.max(sigma_k), np.argmax(sigma_k)+1
    print(argmax)





    
