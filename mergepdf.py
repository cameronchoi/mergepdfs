from PyPDF2 import PdfFileMerger
import sys
import os
from pprint import pprint
import re

if len(sys.argv) < 2:
    print('Please input a directory to merge pdfs')
    sys.exit(1)


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]


for dirpath, dirnames, filenames in os.walk(sys.argv[1]):

    filenames.sort(key=natural_keys)

    pdfs = []

    for file in filenames:
        if file != 'result.pdf' and re.search('\.pdf$', file):
            pdfs.append('{}/{}'.format(sys.argv[1], file))

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("{}/result.pdf".format(sys.argv[1]))
    merger.close()
