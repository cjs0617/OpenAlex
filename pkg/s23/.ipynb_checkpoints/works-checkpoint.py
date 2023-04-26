"""work class"""
import base64
import requests
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from IPython.display import display, HTML


class Works:
    """define work class"""

    def __init__(self, oaid):
        self.oaid = oaid
        self.req = requests.get(f"https://api.openalex.org/works/{oaid}")
        self.data = self.req.json()

    def __str__(self):
        return "str"

    @property
    def ris(self):
        fields = []
        if self.data["type"] == "journal-article":
            fields += ["TY  - JOUR"]
        else:
            raise Exception("Unsupported type {self.data['type']}")

        for author in self.data["authorships"]:
            fields += [f'AU  - {author["author"]["display_name"]}']

        fields += [f'PY  - {self.data["publication_year"]}']
        fields += [f'TI  - {self.data["title"]}']
        fields += [f'JO  - {self.data["host_venue"]["display_name"]}']
        fields += [f'VL  - {self.data["biblio"]["volume"]}']

        if self.data["biblio"]["issue"]:
            fields += [f'IS  - {self.data["biblio"]["issue"]}']

        fields += [f'SP  - {self.data["biblio"]["first_page"]}']
        fields += [f'EP  - {self.data["biblio"]["last_page"]}']
        fields += [f'DO  - {self.data["doi"]}']
        fields += ["ER  -"]

        ris = "\n".join(fields)
        ris64 = base64.b64encode(ris.encode("utf-8")).decode("utf8")
        uri = f'<pre>{ris}</pre><br><a href="data:text/plain;base64,{ris64}" download="ris">Download RIS</a>'  # pylint: disable-msg=C0301
        display(HTML(uri))
        return ris

    @property
    def bibtex(self):
        _authors = [au["author"]["display_name"] for au in self.data["authorships"]]
        if len(_authors) == 1:
            authors = _authors[0]
        else:
            authors = ", ".join(_authors[0:-1]) + " and" + _authors[-1]
        title = self.data["title"]
        journal = self.data["host_venue"]["display_name"]
        volume = str(self.data["biblio"]["volume"])
        pages = "-".join(
            [
                self.data["biblio"].get("first_page", "") or "",
                self.data["biblio"].get("last_page", "") or "",
            ]
        )
        year = str(self.data["publication_year"])
        url = self.data["host_venue"]["url"]
        doi = self.data["doi"]
        journal_type = self.data["type"]
        d_b = BibDatabase()
        d_b.entries = [
            {
                "journal": journal,
                "pages": pages,
                "title": title,
                "year": year,
                "volume": volume,
                "author": authors,
                "url": url,
                "doi": doi,
                "ID": title,
                "ENTRYTYPE": journal_type,
            }
        ]

        writer = BibTexWriter()
        with open("bibtex.bib", "w") as bibfile:
            bibfile.write(writer.write(d_b))
        print(open("bibtex.bib", "r").read())
