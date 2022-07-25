def rna_transcript(strand: str) -> str:
    translations = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    for key in translations:
        if key in strand:
            return translations[key]
    raise ValueError('DNA strand incorrect')
