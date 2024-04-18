# Bib Cleaner
 
BibCleaner is a very simple script that takes a LaTeX source file and multiple BibTex files to produce a new BibTex file containing only used references.

To run it, type:

```sh
python3 bib_cleaner.py [main_latex_file] [bib_file1 bib_file2 ... bib_fileN] > new_bib.bib
```

The goal here is to remove unused references. 

We use the `bibtexparser` in order to deal with BibTex format. So, before running the script:

```sh
pip install -r requirements.txt
```

If you find any issue with this script, please post a Issue on this Github Repo.