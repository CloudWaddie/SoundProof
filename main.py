# Import dependencies - will be packaged in the executable
import argparse
import wave

parser = argparse.ArgumentParser(
                    prog='SoundProof',
                    description='An audio encoder and decoder for secure communication????',
                    epilog='Made by CloudWaddie')
parser.add_argument('filename')  # Input file
args = parser.parse_args()
print(args.filename)