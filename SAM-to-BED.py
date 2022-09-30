'''
OBDS course 
convert SAM file to BED file
authors: Nicole, Matt, Li-Hsin, Susann

read SAM file
output: BED file: column 1 (Chr), column 2(start), column 3(end)
extract column 4 from SAM file (left-most position) --> start-1
        column 9 from SAM file (length of mapping) --> start-1 + length = end
        column 3 from SAM file (Chr)
SAM file: 1-based
BED file: 0-based

command line: python SAM-to-BED.py -i test.sam -o bed_frag --frag

'''

import argparse
import gzip

parser = argparse.ArgumentParser() # Create a parser
parser.add_argument('-o', # Name of option 
                dest='outfile', # Variable name to store option (optional)
                help='output file name', # Help text (optional)
                )
parser.add_argument('-i', # Name of option short form
                    '--input', # Name of option long form
                    dest='infile', # Variable name to store option (optional)
                    help='Input file name', # Help text (optional)
                    ) 
parser.add_argument('-pad',   #define input argument to pad interval
                    type=int,
                    dest='padnum',
                    default = 0,   #default for 'padnum'
                    )
parser.add_argument('--gzip', 
                    action='store_true',
                    default = False,
                    )
parser.add_argument('--frag',
                    action='store_true',
                    default = False,
                    )

args = parser.parse_args() # Parse arguments


def sam_to_bed(bed):   
        with open(args.infile, mode="r") as sam: # Create file handle   
        
            for i, line in enumerate(sam): # Iterate line by line through the file
                if line[0] !='@':
                    columns = line.strip().split('\t')  #make tuple of columns
                    chr = columns[2]
                    if chr[0] != '*':
                        start = int(columns[3]) -1 -args.padnum
                        end = start + int(len(columns[9])) +args.padnum*2
                        name = columns[0]
                        score = columns[4]
                        strand = '.'
                        bed.write(f'{chr}\t{start}\t{end}\t{name}\t{score}\t{strand}\n')


def output_as_fragments(bed): #function to give coordinates instead of reads
    with open(args.infile, mode="r") as sam: # Create file handle   
        
            for i, line in enumerate(sam): # Iterate line by line through the file
                if line[0] !='@':
                    columns = line.strip().split('\t')  #make tuple of columns
                    chr = columns[2]
                    if chr[0] != '*' and int(columns[8]) > 1:                       
                        start = int(columns[3]) -1 -args.padnum
                        end = start + int(columns[8]) +args.padnum*2
                        name = columns[0]
                        score = columns[4]
                        strand = '.'
                        bed.write(f'{chr}\t{start}\t{end}\t{name}\t{score}\t{strand}\n')


               
if args.gzip==True:
    with gzip.open(args.outfile, mode="wt") as bed:
        if args.frag==True:
            output_as_fragments(bed)
        else:
            sam_to_bed(bed)
else:
    with open(args.outfile, mode="w") as bed:  
        if args.frag==True:
            output_as_fragments(bed)
        else:
            sam_to_bed(bed)


