from scripts.rnatranscript import rna_transcript


def test_rna_transcript_c():
    assert rna_transcript('G') == 'C'
