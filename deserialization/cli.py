import yaml
import argparse 

parser = argparse.ArgumentParser(__name__)
parser.add_argument('-i', '--input')
arguments = parser.parse_args()

with open(arguments.input, 'r') as handle:
    yaml.load(handle)
