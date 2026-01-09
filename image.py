#!/bin/python

import PIL as pil
import numpy as np
from matplotlib import pyplot as plt
from huffman import *
import huffman
goldhill = list(pil.Image.open('./goldhill.png').getdata())
moon = list(pil.Image.open('./moon.png').getdata())
boat = list(pil.Image.open('./boat.png').getdata())

nbins = 256

def entropie(hist, bar_width):
    H = 0
    print("entropie type hits", type(hist))
    for i in range(len(hist)):
        if hist[i] != 0:
            H += hist[i] * np.log2(hist[i])
    H *= -bar_width
    return H
#    return -bar_width * np.sum(hist[hist!=0]*np.log2(hist[hist!=0]))

def encoder_decoder_image(img):
    hist, bin_edges = np.histogram(img, bins=nbins, density=True, range=(0, 255))
    plt.figure()
    bar_width = bin_edges[1]-bin_edges[0]
    plt.bar(bin_edges[ :-1], hist, align='edge', width=bar_width)

    symb = sorted(range(256), key=lambda i:hist[i], reverse=True)
    hist = sorted(hist, reverse=True)
    code, L = huffman_code(hist)
    d = { k:v for k, v in zip(symb, code) }

    print("Hist type : ", type(hist))

    encoded = "".join([d[i] for i in img])
    decoded = decode(encoded, symb, code)
    bits_source = 8*len(img)
    bits_compressed = len(encoded)
    r = bits_compressed/bits_source
    print("Entropie empirique:")
    print(entropie(hist, bar_width))
    print()
    print("Longueur moyenne du code:")
    print(L)
    print()
    print("Ratio de compression:")
    print(r)
    print()
    assert(decoded==img)

print("goldhill.png")
encoder_decoder_image(goldhill)
plt.title("goldhill")

print("moon.png")
encoder_decoder_image(moon)
plt.title("moon")

print("boat.png")
encoder_decoder_image(boat)
plt.title("boat")



plt.show()
