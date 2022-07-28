def rna_transcript(strand: str) -> str:
    translations = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna_strand = "".join(map(lambda k: translations.get(k, ''), strand))
    if len(rna_strand) == len(strand):
        return rna_strand
    else:
        raise ValueError('DNA strand incorrect')
