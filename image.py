import PIL as pil
import numpy as np
from matplotlib import pyplot as plt
from huffman import *
import huffman
goldhill = list(pil.Image.open('./goldhill.png').getdata())
moon = list(pil.Image.open('./moon.png').getdata())
boat = list(pil.Image.open('./boat.png').getdata())

nbins = 256

def encoder_decoder(img):
    hist, bin_edges = np.histogram(img, bins=nbins, density=True)
    plt.figure()
    bar_width = bin_edges[1]-bin_edges[0]
    plt.bar(bin_edges[ :-1], hist, align='edge', width=bar_width)

    symb = sorted(range(256), key=lambda i:hist[i], reverse=True)
    hist = sorted(hist, reverse=True)
    code, L = huffman_code(hist)
    code.sort(key=len)
    d = { k:v for k, v in zip(symb, code) }

    encoded = "".join([d[i] for i in img])
    decoded = decode(encoded, symb, code)
    assert(decoded==img)

encoder_decoder(goldhill)
plt.show()
