#!/usr/bin/env python3
import sys
import os
import random

args = sys.argv
if len(args) != 4:
    print("usage", args[0], "<program> <input_file> <output_file>")
    sys.exit(1)

program_file = args[1]
input_file = args[2]
output_file = args[3]
tmp_file = "tmp.out"

os.system(f"./{program_file} < {input_file} > {tmp_file}")

tmp = open(tmp_file, "r")
out = open(output_file, "r")

for l_tmp, l_out in zip(tmp.readlines(), out.readlines()):
    if l_tmp != l_out:
        print("TEST FAILED!")
        sys.exit(2)
        
print("TEST OK!")


