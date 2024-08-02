import argparse
import os, sys
from HuffmanCompression import getHuffmanCodes, encode 

def Main(args):
    print("\n        --- File Compressor --- \n")

    # switch cases for optional arguments
    
    if args.encode:
        '''
        COMPRESS
        '''
        fileName = args.encode
        print(f"      encoding...\n")
        with open(fileName) as f:
            content = f.read()
            huffman_codes = getHuffmanCodes(content)
            # for c,b in huffman_codes.items():
            #     print(f"char: {c}, code: {b}")
            # print(huffman_codes)
            binary_code = encode(huffman_codes, content)
            outputFile = "output/" + os.path.splitext(os.path.basename(fileName))[0] + ".encoded"
            print(f"      encoded file: {outputFile}\n")
            with open(outputFile, 'w') as outFile:
                outFile.write(f"{huffman_codes}\n")
                outFile.write(f"{binary_code}")
        return
    elif args.decode:
        '''
        DECOMPRESS
        '''
        print("      decoding...\n")
        pass
    elif args.test:
        '''
        RUN TEST CASES
        '''
        pass
    elif args.clean:
        print("      cleaning output...\n")
        CleanOutput()

    return

def CleanOutput():
    folder = 'output/'
    extensions = ['.encoded', '.decoded']
    for file in os.listdir(folder):
        filePath = os.path.join(folder, file)
        
        if os.path.isfile(filePath) and os.path.splitext(filePath)[1] in extensions:
            os.remove(filePath)
            print(f"      removed: {filePath}")
    pass

def SetupArgs():
    argParser = argparse.ArgumentParser(
        prog="FileCompressor.py",
        description="compresses a text file using Huffman Codes to encode/decode the text"
    )
    # argParser.add_argument(
    #     'file',
    #     type=str,
    #     help='-- provide a file to encode/decode'
    # )
    argParser.add_argument(
        '-e',
        '--encode',
        metavar='filename',
        help=' -- encode the file'
    )
    argParser.add_argument(
        '-d',
        '--decode',
        metavar='filename',
        help=' -- decode the file'
    )
    argParser.add_argument(
        '-t',
        '--test',
        action='store_true',
        help=' -- run the test suite'
    )
    argParser.add_argument(
        '-c',
        '--clean',
        action='store_true',
        help=' -- cleans the output directory'
    )
    args = argParser.parse_args()

    if len(sys.argv) == 1:
        argParser.print_help()
        sys.exit(1)
    
    return args

if __name__ == '__main__':
    args = SetupArgs()
    Main(args)
    pass
