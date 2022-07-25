from scripts.rnatranscript import rna_transcript
import pytest


def test_rna_transcript_c():
    assert rna_transcript('G') == 'C'


def test_rns_transcript_returns_G():
    assert rna_transcript('C') == 'G'


def test_rns_transcript_returns_A():
    assert rna_transcript('T') == 'A'


def test_rns_transcript_returns_U():
    assert rna_transcript('A') == 'U'


def test_rns_transcript_returns_error():
    with pytest.raises(ValueError):
        rna_transcript('X') == ValueError('DNA strand incorrect')
