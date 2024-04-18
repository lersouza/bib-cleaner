import argparse
import itertools
import re
import sys

import bibtexparser

ref_in_paper = set()
ref_in_bib = set()


def run(paper_file_path, bibtex_file_paths, show_missing):
    with open(paper_file_path) as paper_file:
        for line in paper_file:
            citations_in_line = {ref for cite in re.findall(r"cite[t,p]{0,1}\{([\w\-\,]+)\}", line) for ref in cite.split(",")}
            ref_in_paper.update(citations_in_line)

    bibtex_entries = [bibtexparser.parse_file(bib_file).entries for bib_file in bibtex_file_paths]

    for entry in itertools.chain.from_iterable(bibtex_entries):
        if entry.key in ref_in_paper:
            sys.stdout.write(entry.raw)
            sys.stdout.write("\r\n")

            ref_in_bib.add(entry.key)

    if show_missing:
        print()
        print("Missing References:")
        print(ref_in_paper - ref_in_bib)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("paper_file", type=str)
    parser.add_argument("bibtex_files", nargs="+", type=str)

    parser.add_argument("--show_missing", action="store_true")

    args = parser.parse_args()

    run(args.paper_file, args.bibtex_files, args.show_missing)
