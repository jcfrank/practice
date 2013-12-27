from tree import TreeNode

class EncodeDict(object):
    encdict = {}

def encode(message):
    tlist = __getcharlist(message)
    # create Huffman tree
    root = getHuffmanTree(tlist)
    # create encode dict
    dictobj = EncodeDict()
    fillEncodeDict(root[0], dictobj)
    # encode message
    encoded = ''
    for c in message:
        encoded = encoded + dictobj.encdict[c]
    return dictobj.encdict, encoded

def decode(encdict, message):
    invdict = {v:k for k, v in encdict.items()}
    res = ''
    keyword = ''
    inx = 0
    while inx <= len(message) - 1:
        keyword = message[inx]
        while not invdict.__contains__(keyword):
            inx += 1
            keyword = keyword + message[inx]
        res = res + invdict.get(keyword)
        inx += 1
    return res

def __getcharlist(message):
    cdict = {}
    for c in message:
        if not cdict.__contains__(c):
            node = TreeNode()
            node.data = c
            node.count = 1
            cdict[c] = node
        else:
            cdict[c].count += 1
    return list(cdict.copy().values())

def getHuffmanTree(nodelist):
    tlist = nodelist.copy()
    while not len(tlist) == 1:
        tlist.sort(key=lambda treenode: treenode.count)
        node1 = tlist.pop(0)
        node2 = tlist.pop(0)
        newnode = TreeNode()
        newnode.count = node1.count + node2.count
        if node1.count >= node2.count:
            newnode.left = node1
            newnode.right = node2
        else:
            newnode.left = node2
            newnode.right = node1
        tlist.append(newnode)
    return tlist

def fillEncodeDict(root, dictionary):
    # walk the tree and update its encode dict.
    __recursiveWalk(root, '', dictionary=dictionary)
    __printDict(dictionary.encdict)

def __recursiveWalk(node, code, dictionary):
    if node.left is not None:
        __recursiveWalk(node.left, code = code + '0', dictionary=dictionary)
    
    if node.right is not None:
        __recursiveWalk(node.right, code = code + '1', dictionary=dictionary)
    
    if node.left is None and node.right is None:
        #print('node:' + node.data + ', code:' + code)
        dictionary.encdict[node.data] = code

def __printDict(encdict):
    print('print encode dict.')
    print(str(encdict))
