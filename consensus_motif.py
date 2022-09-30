
motif_list = ['ATCCAGCT', 'GGGCAACT', 'ATGGATCT', 'AAGCAACC', 'TTGGAACT', 'ATGCCATT', 'ATGGCACT']
length = len(motif_list[0])
position = {}
for pos in range(0,length):
    table = {'A':0, 'T':0, 'G':0 , 'C':0}
    for sequence in motif_list:
        if sequence[pos] == 'A':
            table['A'] +=1
    for sequence in motif_list:
        if sequence[pos] == 'T':
            table['T'] +=1
    for sequence in motif_list:
        if sequence[pos] == 'G':
            table['G'] +=1
    for sequence in motif_list:
        if sequence[pos] == 'C':
            table['C'] +=1
    position[pos] = table
print(position)       

for pos, table in position.items(): 
    for base, count in table.items():
        print(f'{base} {count}')



