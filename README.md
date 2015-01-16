Practice
========

This is the place for my practice projects.

Huffman
----

My practice project after re-visited the idea of Huffman tree in Data structure.

### how-to

Both tree.py and huffman.py are needed.

    import huffman
    
    # a tuple with dict and coded message will return
    codetuple = huffman.encode('some words to be encoded.')
    
    # decode takes two args, an encode dict and a coded message.
    decodemessage = huffman.decode(codetuple[0], codetuple[1])

encode() takes str and returns the encoding dict and encoded message.
decode() takes dict and str and returns the decoded message.

### TODO

1. test it with an actual full-text document.

1. unit tests.

1. make it able to encode/decode actual files.

Find Primes
-----------

Just a practice of a typical problem.

