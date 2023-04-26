from s23 import Works

ref_bibtex = """@journal-article{Examples of Effective Data Sharing in Scientific Publishing,
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
    w = Works("https://doi.org/10.1021/acscatal.5b00538")
    w.bibtex
    captured = capsys.readouterr()
    assert captured.out == ref_bibtex
