practice
========

my python practice project

huffman
====

My practice project after re-visited the Huffman code in Data structure.

how-to
----

Both tree.py and huffman.py are needed.

    import huffman
    
    # a tuple with dict and coded message will return
    codetuple = huffman.encode('some words that needs to encode')
    
    # decode taskes two args, a encode dict and a coded message.
    decodemessage = huffman.decode(codetuple[0], codetuple[1])
  
The function will return a tuple. First value is a dict that contains encode info.
The second is the encoded bits.
