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
            soundproof = SoundProofObject(args.filename)
            soundproof.decode()
            
class SoundProofObject:
    def __init__(self, filename):
        self.filename = filename
        self.wavefile = wave.open(filename, 'rb')
    def decode(self):
        print('Decoding...')
        self.nframes = self.wavefile.getnframes()
        self.channels = self.wavefile.getnchannels()
        if self.channels == 2:
            print('Error: Stereo audio not supported')
            print('This audio has not been encoded correctly')
            exit("Exited. Reason: Stereo audio not supported")
        print(self.nframes)
        # Create an empty dictionary for the table
        table = {}

        # Populate the table
        for i in range(256):
            table[i] = chr(i)
        for frame in range(self.nframes):
            currentframe = self.wavefile.readframes(1)
            # Take the first byte of the frame and convert it to an integer
            byte = currentframe[0]
            # Convert the byte to an ASCII character using the table
            ascii_char = table[byte]
            print(ascii_char)
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