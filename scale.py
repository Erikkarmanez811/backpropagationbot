import numpy as np
import matplotlib.pylab as plt
from PIL import Image
def find_splice(size):
    delta = size % 27
    D = size // 27
    x = size / 27
    while D > delta:
        delta += 27
        D -= 1
    return (max(D,delta),min(D,delta))
def white_to_black(img):
    return np.ones_like(img) - img
def rescale(name, scale):
    img_origin = Image.open('sent_photo/'+name+'.png')
    img_origin.save('sent_photo/'+name+'.png')
    img = plt.imread('sent_photo/'+name+'.png')
    img_gray = white_to_black((1 / 3) * img[:, :, 0] + (1 / 3) * img[:, :, 1] + (1 / 3) * img[:, :, 2])

    size = (len(img_gray), len(img_gray[0]))
    splice_x = find_splice(size[0])
    splice_y = find_splice(size[1])
    new_img = np.zeros((scale, scale))
    for i in range(scale):
        for j in range(scale):
            x_b, x_e = splice_x[1] * i, splice_x[0] + splice_x[1] * i
            y_b, y_e = splice_y[1] * j, splice_y[0] + splice_y[1] * j
            bite = img_gray[x_b:x_e, y_b:y_e]
            new_img[i, j] = np.mean(bite)
    plt.imsave('rescale_photo/'+name+'_s.png',new_img,cmap = 'gray')
    return new_img
def rescale_2(name, scale):
    img_origin = Image.open('sent_photo/'+name+'.png')
    img_origin.save('sent_photo/'+name+'.png')
    img = plt.imread('sent_photo/'+name+'.png')
    size = (len(img), len(img[0]))
    splice_x = find_splice(size[0])
    splice_y = find_splice(size[1])
    new_img = np.zeros((scale, scale,3))
    for i in range(scale):
        for j in range(scale):
            x_b, x_e = splice_x[1] * i, splice_x[0] + splice_x[1] * i
            y_b, y_e = splice_y[1] * j, splice_y[0] + splice_y[1] * j
            for channel in range(3):
                bite = img[x_b:x_e, y_b:y_e,channel]
                new_img[i, j,channel] = np.mean(bite)
    plt.imsave('rescale_photo/'+name+'_s.png',new_img,cmap = 'gray')
    return new_img
