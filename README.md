# pagelabels
Python utility to manipulate PDF page labels.

A useful but rarely-used feature of PDFs is the ability to use
custom naming schemes for pages. This allows to start a PDF at
any given page number instead of 1, to restart page numbering 
for each section of a long PDF, or to attribute a certain name
to a given page.

![Example page labels generated with pagelabels and viewed in evince](https://user-images.githubusercontent.com/552629/48559767-88368380-e8ec-11e8-827c-068c1d34c588.png)

## Addpagelabels utility
### Installation
#### Dependencies
Install **pip** if you don't have it already:
```bash
$ sudo apt install python3-pip
```
Install [**pdfrw**](https://github.com/pmaupin/pdfrw):
```
$ pip3 install --user pdfrw
```

#### The script
```
$ git clone https://github.com/lovasoa/pagelabels-py.git
```
### How to use
Get to the directory where you cloned the script:
```
$ cd pagelabels-py
```

#### Add a new page index to the PDF
This reads the file `/tmp/test.pdf`,
and creates a copy of it with new page labels
without deleting the ones that may already exist.
The new index will take effect from the 1st page of the PDF,
will be composed of uppercase roman numerals, preceded by the string "Intro ",
and starting from "V".

Page numbers will be: "Intro V", "Intro VI", "Intro VII", ...
```
$ ./addpagelabels.py --startpage 1 --type "roman uppercase" --prefix "Intro " --firstpagenum 5 --outfile /tmp/new.pdf /tmp/test.pdf
```

#### Print usage info
```
$ ./addpagelabels.py -h
```

This should print:
```
usage: addpagelabels.py [-h] [--delete] [--startpage STARTPAGE]
                        [--type {arabic,roman lowercase,roman uppercase,letters lowercase,letters uppercase}]
                        [--prefix PREFIX] [--firstpagenum FIRSTPAGENUM]
                        [--outfile out.pdf]
                        file.pdf

Add page labels to a PDF file

positional arguments:
  file.pdf              the PDF file to edit

optional arguments:
  -h, --help            show this help message and exit
  --delete              delete the existing page labels
  --startpage STARTPAGE, -s STARTPAGE
                        the index (starting from 1) of the page of the PDF
                        where the labels will start
  --type {arabic,roman lowercase,roman uppercase,letters lowercase,letters uppercase}, -t {arabic,roman lowercase,roman uppercase,letters lowercase,letters uppercase}
                        type of numbers: arabic = 1, 2, 3, roman = i, ii, iii,
                        iv, letters = a, b, c
  --prefix PREFIX, -p PREFIX
                        prefix to the page labels
  --firstpagenum FIRSTPAGENUM, -f FIRSTPAGENUM
                        number to attribute to the first page of this index
  --outfile out.pdf, -o out.pdf
                        Where to write the output file
```

#### Delete existing page labels from a PDF
```
$ ./addpagelabels.py --delete file.pdf
```

### Complete example
Let's say we have a PDF named `my_document.pdf`, that has 12 pages.
 * Pages 1 to 4 should be labelled `Intro I` to `Intro IV`.
 * Pages 5 to 9 should be labelled `2` to `6`.
 * Pages 10 to 12 should be labelled `Appendix A` to `Appendix C`.

We can issue the following list of commands:

```bash
./addpagelabels.py --delete "my_document.pdf"
./addpagelabels.py --startpage 1 --prefix "Intro " --type "roman uppercase" "my_document.pdf"
./addpagelabels.py --startpage 5 --firstpagenum 2 "my_document.pdf"
./addpagelabels.py --startpage 10 --prefix "Appendix " --type "letters uppercase" "my_document.pdf"
```

## Usage as a python library
This project can be used as a python library.
See [*pagelabels* on the python package index](https://pypi.org/project/pagelabels/).