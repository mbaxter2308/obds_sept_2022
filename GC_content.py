sequence = 'TATAATGCTGACTTATAGCGCTATATATATATA'
GC = 0
TA = 0

for base in sequence:
    if base == "G" or base == "C":
        GC+=1
    else:
        TA+=1
print(GC/(GC+TA)*100)

