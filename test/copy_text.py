import os
import shutil
from os.path import join

# By entering the 'raw_input'
input = raw_input("Please enter the source file name:   ")
Destination = raw_input("Please enter the target file name:     ")

try:
    os.path.exists(Destination)

except Exception as IOError:
    os.path.exists(Destination)

# Copy the file into the target Directory
try:
    shutil.copytree(input, Destination)
    print ("The file Copied Successfully -->", Destination)

except Exception as IOError:
    if (os.path.exists(input)):
        print ("The file is Already exists", Destination)
    else:
        print ("The file not found")

