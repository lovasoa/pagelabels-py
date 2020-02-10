#!/usr/bin/env python3

import argparse
from pathlib import Path

from pdfrw import PdfReader, PdfWriter

from . import PageLabels, PageLabelScheme

parser = argparse.ArgumentParser(
        prog='pagelabels',
        description='Add page labels to a PDF file')
parser.add_argument('file', type=Path, metavar="file.pdf",
                    help='the PDF file to edit')
parser.add_argument("--outfile", "-o", type=Path, default=None, metavar="out.pdf",
                    help="Where to write the output file")

action_group = parser.add_mutually_exclusive_group()
action_group.add_argument('--delete', action='store_true',
                    help='delete the existing page labels')
action_group.add_argument('--update', action='store_true',
                    help='change all the existing page numbering schemes instead of adding a new one')

parser.add_argument('--startpage', '-s', type=int, default=1,
                    help="the index (starting from 1) of the page of the PDF where the labels will start")
parser.add_argument('--type', "-t", choices=PageLabelScheme.styles(),
                    help="""type of numbers:
                                arabic  = 1, 2,  3,
                                roman   = i, ii, iii, iv,
                                letters = a, b, c""")
parser.add_argument("--prefix", "-p", 
                    help="prefix to the page labels")
parser.add_argument("--firstpagenum", "-f", type=int, default=1,
                    help="number to attribute to the first page of this index")
parser.add_argument('--load', type=Path, metavar='other.pdf',
                    help='copy page number information from the given PDF file')
options = parser.parse_args()

reader = PdfReader(str(options.file.resolve()))

if options.load:
    other = PdfReader(str(options.load.resolve()))
    labels = PageLabels.from_pdf(other)
elif options.delete:
    labels = PageLabels()
elif options.update:
    labels = PageLabels(
        label._replace(
            style=options.type or label.style,
            prefix=options.prefix or label.prefix
        ) if label.startpage >= options.startpage - 1 else label
        for label in PageLabels.from_pdf(reader)
    )
else:
    labels = PageLabels.from_pdf(reader)
    newlabel = PageLabelScheme(startpage=options.startpage - 1,
                               style=options.type or "arabic",
                               prefix=options.prefix or "",
                               firstpagenum=options.firstpagenum)
    labels.append(newlabel)
# Write the new page labels to the PDF
labels.write(reader)
print("New labels to be written:")
print("\n".join(map(str, labels)))

writer = PdfWriter()
writer.trailer = reader
outfile = options.outfile or options.file
writer.write(str(outfile.resolve()))
print("Resulting pdf file created : {}".format(outfile))
