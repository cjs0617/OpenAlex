"""Bibtex Testing"""

from s23 import Works  # pylint: disable-msg=E0611

REF_BIBTEX = """@journal-article{Examples of Effective Data Sharing in Scientific Publishing,
 author = {John R. Kitchin},
 doi = {https://doi.org/10.1021/acscatal.5b00538},
 journal = {ACS Catalysis},
 pages = {3894-3899},
 title = {Examples of Effective Data Sharing in Scientific Publishing},
 url = {https://doi.org/10.1021/acscatal.5b00538},
 volume = {5},
 year = {2015}
}

"""


def test_bibtex(capsys):
    """Compare reference with output"""
    w_self = Works("https://doi.org/10.1021/acscatal.5b00538")
    w_self.bibtex  # pylint: disable-msg=W0104
    captured = capsys.readouterr()
    assert captured.out == REF_BIBTEX
