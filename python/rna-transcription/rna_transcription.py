def to_rna(dna_strand):
    dnaXRna = {'G' : 'C', 'C' : 'G', 'T' : 'A', 'A' : 'U'}
    rna_strand = ''

    #for n in dna_strand:
    #    rna_strand += dnaXRna[n]

    return ''.join(list(map(lambda s: dnaXRna[s],dna_strand)))

