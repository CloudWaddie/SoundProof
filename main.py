# Import dependencies - will be packaged in the executable
import argparse
import wave

parser = argparse.ArgumentParser(
                    prog='SoundProof',
                    description='An audio encoder and decoder (for hiding messages in audio files).',
                    epilog='Made by CloudWaddie')
parser.add_argument('-t', help='Encode/Decode a file', metavar='ENCODE/DECODE', required=True)
parser.add_argument('filename', help='File to encode/decode', metavar='FILENAME')
## Not needed: parser.add_argument('--decode', help='Decode a file', metavar='FILENAME')
args = parser.parse_args()
try:
    print(args.filename)
    if args.t.lower() == 'decode':
        print('Decoding...')
        loadfile = wave.open(args.filename, 'rb')
except argparse.ArgumentError:
    print()
    print('No file specified\nRun with --help for more info')
    exit("Exited. Reason: No file specified")