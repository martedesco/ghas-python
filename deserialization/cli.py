import os
import yaml
import pickle
import argparse 

parser = argparse.ArgumentParser(__name__)
parser.add_argument('-i', '--input', required=True)
arguments = parser.parse_args()


if arguments.input.endswith('.yml'):
    with open(arguments.input, 'r') as handle:
        yaml.load(handle)

elif arguments.input.endswith('.pickle'):
    with os.open(arguments.input, 'r') as handle:
        pickle.load(handle)
