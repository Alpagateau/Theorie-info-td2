class Node:
    def __init__(self, l = None, r = None, i = 0, p = 0):
        self.l : Node = l
        self.r : Node = r
        self.i : Int = i
        self.p : Float = p
        self.symbol = None
    
    def __str__(self):
        return "( "+str(self.p)+ "("+str(self.i)+"): " +str(self.l) + " | " + str(self.r) +" )"

def huffman_tree(p):
    trees = [Node(None, None, 0, pro) for pro in p]
    while len(trees) > 1:
        trees.sort(reverse = True, key = lambda x : x.p)
        t1 = trees[-1]
        t2 = trees[-2]
        trees = trees[:-2] + [Node(t2, t1, 0, t2.p + t1.p)]
    t = trees[0]
    tag_tree(t, 0)
    return t

def get_cwd(tree):
    if tree == None: 
        return [""]
    if tree.l == None and tree.r == None:
        return [""]
    return ["0" + s for s in get_cwd(tree.l)] +["1" + s for s in get_cwd(tree.r)]

def tag_tree(tree, acc, symbols = []):
    if tree.l == None and tree.r == None:
        tree.i = acc
        if symbols != []:
            tree.symbol = symbols[acc]
        return acc+1
    
    acc = tag_tree(tree.l, acc)
    acc = tag_tree(tree.r, acc)
    return acc

def huffman_code(p):
    tree = huffman_tree(p) 
    words = get_cwd(tree)
    return (words, sum([len(w)/len(words) for w in words]))

def huffman_tree2(cwd, symbol = ""):
    if len(cwd) == 0:
        n = Node(None, None, 0, 0)
        n.symbol = symbol
        return  n
    cwdl = [i[1:] for i in cwd if len(i) > 1 and i[0] == "0"]
    cwdr = [i[1:] for i in cwd if len(i) > 1 and i[0] == "1"] 
    return Node(huffman_tree2(cwdl, symbol + "0"), huffman_tree2(cwdr, symbol + "1"), 0, 0)

#def cwd_detect(tree, seq):
#

a = huffman_tree([0.1, 0.1, 0.15, 0.16, 2])
cdw = get_cwd(a)
print(a)
print(huffman_code([0.1, 0.1, 0.15, 0.16, 2]))
b = huffman_tree2(cdw)
print(b)
