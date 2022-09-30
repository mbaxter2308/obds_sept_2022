sequence = 'TATAATGCTGACTTATAGCGCTATATATATATA'
motif = 'TATA'
length = len(motif)
pos = 0
sum = 0
for base in sequence:
    if sequence[pos:pos + length] == motif:
        print(f'start: {pos+1}, end: {pos + length}')
        sum+=1
    pos+=1
print(f'number of occurences: {sum}')


    