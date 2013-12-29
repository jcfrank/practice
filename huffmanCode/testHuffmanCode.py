import unittest
import huffman

class TestHuffmanFunctions(unittest.TestCase):

    def setUp(self):
        self.filepath = '_testfiles/textfile1.txt'

    def test_encode_text(self):
        print('test_encode_text')
        huffman.DEBUG = True
        print('huffman.DEBUG=' + str(huffman.DEBUG))
        path = self.filepath
        with open(path, 'r+') as f:
            eof = False
            while not eof:
                line = f.readline()
                if len(line) == 0:
                    eof = True
                    break
                coded = huffman.encode(line)
                decoded = huffman.decode(coded[0], coded[1])
                self.assertEqual(line, decoded)

if __name__ == '__main__':
    unittest.main()

