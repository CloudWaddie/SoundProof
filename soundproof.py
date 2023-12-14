# Import dependencies - will be packaged in the executable
import argparse
import wave
import os

def init():
    print('SoundProof v2.0')
    print('Made by CloudWaddie')
    print('==================')
def decode():
        soundproof = SoundProofObject(args.filename)
        soundproof.decode()
def encode():
    soundproof = SoundProofObject(args.filename)
    message = input('Enter message to encode: ')
    soundproof.encode(message)
    soundproof.wavefile.close()
def getinput(userinput, type):
    soundproofinput = SoundProofObject(userinput)
    if type == 'encode':
        message = input('Enter message to encode: ')
        soundproofinput.encode(message)
        soundproofinput.input(userinput)
    else:
        print('INPUT can only be used with type ENCODE')
        exit("Exited. Reason: INPUT can only be used with type ENCODE")
            
class SoundProofObject:
    def __init__(self, filename):
        self.filename = filename
        # Get the directory name from the filename
        dirname = os.path.dirname(filename)
        # If the directory doesn't exist, create it
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)
    def decode(self):
        try:
            self.wavefile = wave.open(self.filename, 'rb')  # Change 'wb' to 'rb' for reading
        except wave.Error:
            print('Error: File is not a .wav file')
            exit("Exited. Reason: File is not a .wav file")
        print('Decoding...')
        # Create an empty string to store the decoded message
        message = ''
        # Get the number of frames from the wave file
        self.nframes = self.wavefile.getnframes()
        # Read the frames of the wave file
        for _ in range(self.nframes):
            currentframe = self.wavefile.readframes(1)
            # Take the first byte of the frame and convert it to an integer
            byte = currentframe[0]
            # Convert the byte to an ASCII character and add it to the message
            message += chr(byte)
        print('Message decoded from ' + self.filename + ': ' + message)
    def encode(self, message):
        try:
            self.wavefile = wave.open(self.filename, 'wb')
        except wave.Error:
            print('Error: File is not a .wav file')
            exit("Exited. Reason: File is not a .wav file")
        print('Encoding...')
        # Set the parameters of the new wave file to match the original
        self.wavefile.setparams((1, 1, 44100, 0, 'NONE', 'not compressed'))
        # Convert the message to bytes and write it to the new wave file
        for char in message:
            self.wavefile.writeframes(bytes([ord(char)]))
        print('Message encoded to ' + self.filename)
    def input(self, input):
        pass

init()

parser = argparse.ArgumentParser(
                    prog='SoundProof',
                    description='An audio encoder and decoder (for hiding messages in audio files).',
                    epilog='Made by CloudWaddie')
parser.add_argument('-t', help='Encode/Decode a file', metavar='ENCODE/DECODE')
parser.add_argument('filename', help='File to encode/decode', metavar='FILENAME')
parser.add_argument('--version', '-v', action='version', version='Current version is %(prog)s 2.0 beta') 
parser.add_argument('--input', '-i', help='Input file', metavar='INPUTFILE')
# Not needed: parser.add_argument('--decode', help='Decode a file', metavar='FILENAME')
args = parser.parse_args()
def runmain():
    #bypasses
    try:
        if args.input and os.path.exists(args.input):
            print('Input file: ' + args.input)
            gettype = args.t.lower()
            getinput(args.input, gettype)
            
        elif args.input and not os.path.exists(args.input):
            print('Error: Input file does not exist')
            exit("Exited. Reason: Input file does not exist")
        else:
            print('No input file specified')
        if args.t.lower() == 'decode':
            decode()
        elif args.t.lower() == 'encode':
            encode()
    except argparse.ArgumentError:
        print()
        print('No file specified\nRun with --help for more info')
        exit("Exited. Reason: No file specified")
runmain()