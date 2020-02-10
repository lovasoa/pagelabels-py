# pagelabels
Python utility to manipulate PDF page labels.

A useful but rarely-used feature of PDFs is the ability to use
custom naming schemes for pages. This allows to start a PDF at
any given page number instead of 1, to restart page numbering 
for each section of a long PDF, or to attribute a certain name
to a given page.

![Example page labels generated with pagelabels and viewed in evince](https://user-images.githubusercontent.com/552629/48559767-88368380-e8ec-11e8-827c-068c1d34c588.png)

## Addpagelabels utility
PDF files can contain one ore more page numbering schemes.
Each scheme has a start page, specifying the page where it should take
effect. All subsequent pages will be affected by the scheme,
until another page numbering scheme is encountered.
This utility allows adding, removing, and updating page numbering schemes
in a PDF file.

### Installation
#### Dependencies

Install **pip** if you don't have it already:
##### On Linux
```bash
$ sudo apt install python3-pip
```

##### On MacOS
Install [brew](https://brew.sh/), and then install python:

```bash
brew install python
```

##### On Windows
Install [WSL](https://docs.microsoft.com/en-us/windows/wsl/about)
and then follow the linux instructions.

#### The script
Install **pagelabels-py** :
```
python3 -m pip install --user --upgrade pagelabels 
```

### How to use

#### Add a new page index to the PDF
This reads the file `/tmp/test.pdf`,
and creates a copy of it with new page labels
without deleting the ones that may already exist.
The new index will take effect from the 1st page of the PDF,
will be composed of uppercase roman numerals, preceded by the string "Intro ",
and starting from "V".

Page numbers will be: "Intro V", "Intro VI", "Intro VII", ...
```
python3 -m pagelabels --startpage 1 --type "roman uppercase" --prefix "Intro " --firstpagenum 5 --outfile /tmp/new.pdf /tmp/test.pdf
```

#### Print usage info
```
python3 -m pagelabels -h
```

This should print:
```
usage: pagelabels [-h] [--outfile out.pdf] [--delete | --update]
                  [--startpage STARTPAGE]
                  [--type {arabic,roman lowercase,roman uppercase,letters lowercase,letters uppercase}]
                  [--prefix PREFIX] [--firstpagenum FIRSTPAGENUM]
                  file.pdf

Add page labels to a PDF file

positional arguments:
  file.pdf              the PDF file to edit

optional arguments:
  -h, --help            show this help message and exit
  --outfile out.pdf, -o out.pdf
                        Where to write the output file
  --delete              delete the existing page labels
  --update              change all the existing page numbering schemes instead
                        of adding a new one
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
```

#### Delete existing page labels from a PDF
```
python3 -m pagelabels --delete file.pdf
```

#### Copy page labels from one PDF to another
The following will take the page labelling scheme from `source.pdf` and 
apply it to `target.pdf` :
```
python3 -m pagelabels --load source.pdf target.pdf
```

### Complete example: creating a PDF with several different page numbering styles
Let's say we have a PDF named `my_document.pdf`, that has 12 pages.
 * Pages 1 to 4 should be labelled `Intro I` to `Intro IV`.
 * Pages 5 to 9 should be labelled `2` to `6`.
 * Pages 10 to 12 should be labelled `Appendix A` to `Appendix C`.

We can issue the following list of commands:

```bash
python3 -m pagelabels --delete "my_document.pdf"
python3 -m pagelabels --startpage 1 --prefix "Intro " --type "roman uppercase" "my_document.pdf"
python3 -m pagelabels --startpage 5 --firstpagenum 2 "my_document.pdf"
python3 -m pagelabels --startpage 10 --prefix "Appendix " --type "letters uppercase" "my_document.pdf"
```

### Updating existing page numbers
Let's say we have a PDF with pages named 10, 11, 12, A, B, C
and we want to add a prefix to the labels, while keeping the existing custom
page offset and styles. We can do that using the `--update` option of pagelabels:

```
python3 -m pagelabels --update --prefix "EX-" my_document.pdf
```

This will update the existing labels to EX-10, EX-11, EX-12, EX-A, EX-B, EX-C.

## Warning
*pagelabels-py* internally uses [pdfrw](https://github.com/pmaupin/pdfrw), that can write only [**PDF version 1.3**](https://en.wikipedia.org/wiki/History_of_the_Portable_Document_Format_(PDF)). If your PDF uses features that are not compatible with PDF 1.3, you may see it not being rendered correctly after using *pagelabels-py*.

## Usage as a python library
This project can be used as a python library.
See [*pagelabels* on the python package index](https://pypi.org/project/pagelabels/).

