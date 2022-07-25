def rna_transcript(strand: str) -> str:
    translations = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna_strand = ""
    for char in strand:
        if char in translations:
            rna_strand += translations[char]
        else:
            raise ValueError('DNA strand incorrect')
    return rna_strand
