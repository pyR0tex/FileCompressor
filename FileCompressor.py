import argparse
import os, sys
import HuffmanCompression

def Main(args):
    print("\n        --- File Compressor --- \n")

    # switch cases for optional arguments
    fileName = args.file
    if args.compress:
        '''
        COMPRESS
        '''
        with open(fileName) as f:
            content = f.read()
            huffman = HuffmanCompression.compress(content)

    elif args.decompress:
        '''
        DECOMPRESS
        '''
        print("decompress")
        pass
    elif args.test:
        pass
    
def SetupArgs():
    argParser = argparse.ArgumentParser(
        prog="FileCompressor.py",
        description="Compresses a text file using Huffman Codes to encode/decode the text"
    )
    argParser.add_argument(
        'file',
        type=str,
        help='-- provide a file to compress/decompress'
    )
    argParser.add_argument(
        '-c',
        '--compress',
        action='store_true',
        help=' -- compress the file'
    )
    argParser.add_argument(
        '-d',
        '--decompress',
        action='store_true',
        help=' -- decompress the file'
    )
    argParser.add_argument(
        '-t',
        '--test',
        help=' -- run the test suite'
    )
    args = argParser.parse_args()
    return args

if __name__ == '__main__':
    args = SetupArgs()
    Main(args)
    pass
