
import subprocess

myvar = input("What is your name?")

subprocess.run('echo "' + myvar + '"')
