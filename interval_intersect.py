'''
OBDS course 
script to determine number of overlaps between two bed files
author: Matt Baxter

description: 
Find the number of overlaps which file_a and file_b share. 
Report the number of overlaps. 
Create .bed file listing the regions from file_a which intersected. 

command line example: 
python intervall_intersection.py -o [OUTFILE.bed] -a [INFILE_A].bed -b [INFILE_B].bed 

'''

import argparse
import gzip

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
                            break
                        elif start_a >= start_b and start_a <= end_b:
                            bed.write(line_a)
                            count += 1
                            break
                test.seek(0)
    return (count)



with open(args.outfile, mode="w") as bed:
    count=intersect_a_b(bed) 

print(count)    