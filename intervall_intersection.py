'''
OBDS course 
determine overlap of genomic intervals between two bed files
authors: Matt, Susann

read BED files
loop over every line in reference:
    calculate intervals of reference (start to end)
    loop over every line in test:
        if start point of test_sequence is > start_reference and <end_reference write line to output file and break
        if end point of test_sequence is > start_reference and <end_reference write line to output file and break
        else don't write to output file

command line: python intervall_intersection.py -o intersect.bed -a brain_dnase1_chr21.bed -b gut_dnase1_chr21.bed 

'''

import argparse
import gzip
import sys
import logging
import re

parser = argparse.ArgumentParser() # Create a parser
parser.add_argument('-o', # Name of option 
                dest='outfile', # Variable name to store option (optional)
                help='output file name', # Help text (optional)
                )
parser.add_argument('-a', # Name of option short form
                    '--ref_file', # Name of option long form
                    dest='file_a', # Variable name to store option (optional)
                    help='reference file name', # Help text (optional)
                    ) 
parser.add_argument('-b', # Name of option short form
                    '--query_file', # Name of option long form
                    dest='file_b', # Variable name to store option (optional)
                    help='query file name', # Help text (optional)
                    ) 
parser.add_argument('--stdout', 
                    action='store_true',
                    default = False,
                    )
parser.add_argument('--duplicates', 
                    action='store_true',
                    default = False,
                    )

args = parser.parse_args() # Parse arguments


def intersect_a_b(bed):
    count = 0
    with open(args.file_a, mode="r") as reference: # Create file handle   
        with open (args.file_b, mode="r") as test: # Create file handle
            for index_a, line_a in enumerate(reference): # Iterate line by line through the reference file
                col_a = line_a.strip().split('\t')  #make tuple of columns
                start_a = int(col_a[1])
                end_a = int(col_a[2])
                chr_a = col_a[0]
                for index_b, line_b in enumerate(test): # Iterate line by line through the test file
                    col_b = line_b.strip().split('\t')  #make tuple of columns
                    start_b = int(col_b[1])
                    end_b = int(col_b[2])
                    chr_b = col_b[0]
                    if chr_a == chr_b:
                        if start_b >= start_a and start_b <= end_a:
                            bed.write(line_a)
                            count += 1
                            if args.duplicates == False:
                                break       #break as soon as one overlaping interval is found
                        elif start_a >= start_b and start_a <= end_b:
                            bed.write(line_a)
                            count += 1
                            if args.duplicates == False:
                                break       #break as soon as one overlaping interval is found
                test.seek(0)
    return (count)


if args.stdout == True:
    outputfilehandle = sys.stdout
    count = intersect_a_b(outputfilehandle)   
 
else:
    with open(args.outfile, mode="w") as bed:
        count=intersect_a_b(bed) 

print(count)  
