from huffman import *

test_text = "Voici un petit texte tout simple, pour essayer la compression"
elements = [i for i in test_text]
new_dic = {}
for e in elements:
    if e in new_dic.keys():
        new_dic[e] += 1
    else:
        new_dic[e] = 1
new_dic = dict(sorted(new_dic.items(), key=lambda item:item[1]))

symbols = list(new_dic.keys())
probas  = list(new_dic.values())

cwd = sorted( get_cwd(huffman_tree(probas)), key = len)
print(cwd)

convertion_dic1 = { k:v for (k,v) in zip(symbols, cwd)}
convertion_dic2 = { k:v for (k,v) in zip(cwd, symbols)}

words = "".join([convertion_dic1[c] for c in elements])
print(words)

out = decode(words, symbols, cwd)
print(out)

print(avg_length(["101", "1000", "2000"], [0.5, 0.25, 0.25]))
