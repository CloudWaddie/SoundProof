# Import dependencies - will be packaged in the executable
import argparse
import wave

def init():
    print('SoundProof v1.0')
    print('Made by CloudWaddie')
    print('==================')
def decode():
        print(args.filename)
        if args.t.lower() == 'decode':
            print('Decoding...')
            SoundProofObject(args.filename)
            
class SoundProofObject:
     def __init__(self, filename):
         self.filename = filename
         self.wavefile = wave.open(filename, 'rb')
         self.frames = self.wavefile.readframes(-1)
         self.soundproof = self.frames[:44]
         self.message = self.frames[44:]
         self.wavefile.close()
init()

parser = argparse.ArgumentParser(
                    prog='SoundProof',
                    description='An audio encoder and decoder (for hiding messages in audio files).',
                    epilog='Made by CloudWaddie')
parser.add_argument('-t', help='Encode/Decode a file', metavar='ENCODE/DECODE', required=True)
parser.add_argument('filename', help='File to encode/decode', metavar='FILENAME')
# Not needed: parser.add_argument('--decode', help='Decode a file', metavar='FILENAME')
args = parser.parse_args()
try:
    decode()
except argparse.ArgumentError:
    print()
    print('No file specified\nRun with --help for more info')
    exit("Exited. Reason: No file specified")