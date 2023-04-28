"""add command line utility"""
import argparse
from s23oa import Works  # pylint: disable-msg=E0611


def main(parsed_args):
    """define main"""
    work_data = Works(parsed_args.doi)
    if parsed_args.ris:
        print(work_data.ris)

    if parsed_args.bibtex:
        work_data.bibtex  # pylint: disable-msg=W0104


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="command.py script with flags")
    parser.add_argument("doi", help="DOI for the work")
    parser.add_argument("--ris", action="store_true", help="Print RIS data")
    parser.add_argument("--bibtex", action="store_true", help="Print BibTeX data")
    args = parser.parse_args()
    main(args)
