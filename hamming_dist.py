sequence = 'TATAATGCTGACTTATAGCGCTATATATATATA'
rev_sequence =  sequence [::-1]
pos=0
hamming_distance=0


for base in sequence:
    if base != rev_sequence[pos]:
        hamming_distance+=1
    pos+=1

print(hamming_distance)

