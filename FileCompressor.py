import argparse
import os, sys
from collections import Counter

def Main(args):
    print("\n        --- File Compressor --- \n")
    # if input file provided
    if args.File:
        fileName = str(args.File)
        frequency = getFrequency(fileName)
    return

def getFrequency(filename):
    file = filename
    try:
        with open(file) as f:
            content = f.read()
        if not content:
            raise Exception('   file is empty')
        frequency = Counter(content)
        print(f"        Frequencies: \n {dict(frequency)}")
        return frequency
    except Exception as e:
        print(f"     error: {e}")
        sys.exit(1)

def SetupArgs():
    argParser = argparse.ArgumentParser(
        prog="File Compressor",
        description=" -- compresses a text file using Huffman Codes to encode/decode the text"
    )
    argParser.add_argument(
        'File',
        nargs='?',
        help='-- provide a file to compress'
    )
    argParser.add_argument(
        '-t',
        '--test',
        nargs='?',
        help='-- run the test suite'
    )
    args = argParser.parse_args()
    return args

if __name__ == '__main__':
    args = SetupArgs()
    Main(args)
    pass
