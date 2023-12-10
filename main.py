# Import dependencies - will be packaged in the executable
import argparse
import wave

parser = argparse.ArgumentParser(
                    prog='SoundProof',
                    description='An audio encoder and decoder for secure communication????',
                    epilog='Made by CloudWaddie')
parser.add_argument('--encode', help='Encode a file', metavar='FILENAME')
parser.add_argument('--decode', help='Decode a file', metavar='FILENAME')
args = parser.parse_args()
try: print(args.filename)
except: print('No file specified\nRun with --help for more info')