def proteins(strand):
    proteinList = {'Methionine': ['AUG'],
                'Phenylalanine': ['UUU', 'UUC'],
                'Leucine': ['UUA', 'UUG'],
                'Serine': ['UCU', 'UCC', 'UCA', 'UCG'],
                'Tyrosine': ['UAU', 'UAC'],
                'Cysteine': ['UGU', 'UGC'],
                'Tryptophan': ['UGG'],
                'STOP': ['UAA', 'UAG', 'UGA']}
    proteins = list()
    end = False

    for i in range(0,len(strand),3):
        if end: break
        for protein, codon in proteinList.items():
            if strand[i:i+3] in codon:
                if protein == 'STOP':
                    end = True
                    break
                else:
                    proteins.append(protein)

    return proteins

