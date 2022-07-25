from scripts.rnatranscript import rna_transcript


def test_rna_transcript_c():
    assert rna_transcript('G') == 'C'


def test_rns_transcript_returns_G():
    assert rna_transcript('C') == 'G'


def test_rns_transcript_returns_A():
    assert rna_transcript('T') == 'A'
