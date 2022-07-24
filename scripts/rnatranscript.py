def rna_transcript(strand: str) -> str:
    for char in strand:
        if char == 'G':
            return 'C'
