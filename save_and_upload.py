from PIL import Image
import os
import pickle
import numpy as np
import matplotlib.pylab as plt
from scale import rescale,white_to_black
#from bp import Network
def get_array(name):
    img = plt.imread('./' + name)
    return img[:,:]


def create_dataset(name):
    files = os.listdir('C:/Users/white/PycharmProjects/backpropagation/' + name)
    dataset = []
    for i in range(len(files)):
        zero_ar = [0 for i in range(9)]
        zero_ar.insert(int(files[i][10]),1)
        x = (np.array(get_array(name +r'\\'[:-1]+ files[i]))).reshape(784,1)
        y = (np.array(zero_ar)).reshape(10,1)
        dataset.append((x,y))
        dataset.append((white_to_black(x), y))
    return dataset
def get_names(name):
    files = os.listdir('C:/Users/white/PycharmProjects/backpropagation/' + name)
    return files

def save_network(network,text):
    file = open('network_' + text + '.txt', 'wb')
    pickle.dump(network, file)
    file.close()
def open_network(text):
    file = open('network_' + text + '.txt', 'rb')
    network = pickle.load(file)
    file.close()
    return network