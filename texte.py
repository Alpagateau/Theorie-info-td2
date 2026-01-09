import numpy as np
from matplotlib import pyplot as plt
from huffman import *

buscon = list(open('./buscon.txt','r').read())
candide = list(open('./candide.txt','r').read())
dorian = list(open('./dorian.txt','r').read())
clair_de_lune = list(open('./clair-de-lune.txt','r').read())

def entropie(hist):
    H = 0
    print("entropie type hits", type(hist))
    for i in range(len(hist)):
        if hist[i] != 0:
            H += hist[i] * np.log2(hist[i])
    return -H


def count_chars(t):
    d = {  }
    for c in t:
        if not(c in d):
            d[c] = 1
        else:
            d[c] += 1
    symb = sorted(d.keys(), key=lambda k : d[k], reverse=True)
    probas = 1/len(t)*np.array(sorted(d.values(), reverse=True))
    return symb, probas


def encoder_decoder_texte(t):
    symb, probas = count_chars(t)
    code, L = huffman_code(probas)
    code.sort(key=len)
    d = { k:v for k, v in zip(symb, code) }

    encoded = "".join([d[c] for c in t])
    decoded = decode(encoded, symb, code)

    # je pars du principe qu'on utilise la table ASCII donc un caractere fait 8 bits
    bits_source = 8*len(t)
    bits_compressed = len(encoded)
    r = bits_compressed/bits_source
    print("Entropie empirique:")
    print(entropie(probas))
    print()
    print("Longueur moyenne du code:")
    print(L)
    print()
    print("Ratio de compression:")
    print(r)
    print()
    assert(decoded==t)


print("buscon")
encoder_decoder_texte(buscon)

print("candide")
encoder_decoder_texte(candide)

print("dorian")
encoder_decoder_texte(dorian)

print("clair_de_lune")
encoder_decoder_texte(clair_de_lune)

