import argparse
import os, sys
import ast
from HuffmanCompression import encode, decode

def Main(args):
    print("\n  --- File Compressor --- \n")

    # switch cases for optional arguments
    
    if args.encode:
        '''
        COMPRESS
        '''
        fileName = args.encode
        print(f"      encoding...\n")
        with open(fileName) as f:
            content = f.read()
            encoded = encode(content)
            outputFile = "output/" + os.path.splitext(os.path.basename(fileName))[0] + ".encoded"
            print(f"      encoded file: {outputFile}\n")
            with open(outputFile, 'w') as outFile:
                outFile.write(f"{encoded}\n")
        return
    
    if args.decode:
        '''
        DECOMPRESS
        '''
        fileName = args.decode
        if os.path.splitext(os.path.basename(fileName))[1] != ".encoded":
            print("      error: provide a file with extenstion '.encoded' to decode\n")
            sys.exit(1)
        else:
            print("      decoding...\n")
        with open(fileName, 'r') as f:
            content = f.readlines()
            encoded = eval(content[0])
            frequency = encoded["frequency"]
            # huffmanCodes = encoded["codes"]
            binaryCode = encoded["binaryCode"]
            # get the decoded text
            decoded = decode(frequency, binaryCode)

            outputFile = "output/" + os.path.splitext(os.path.basename(fileName))[0] + ".decoded"
            print(f"      decoded file: {outputFile}\n")
            with open(outputFile, 'w') as outFile:
                outFile.write(f"{decoded}")
                
        return
    if args.test:
        '''
        RUN TEST CASES
        '''
        print("      running test cases...\n")
        pass
    if args.clean:
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
