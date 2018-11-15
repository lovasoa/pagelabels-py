# pagelabels python library

This is a little library, based on **pdfrw**, that helps manipulate PDF page labels in python.
It can parse page labels from  a PDF, edit page labels, and write them in a PDF.

For more info about page labels, see: https://www.w3.org/TR/WCAG20-TECHS/PDF17.html

## Classes
 * [PageLabels](#pagelabels)
 * [PageLabelScheme](#pagelabelscheme)

## PageLabels
Inherits from list and represents a list of `PageLabelScheme`s.

### PageLabels.from_pdf(pdfrwobj)
Static method.
Read page labels from a PdfReader object.

### .write(pdfrwobj)
Write the page labels to a PdfReader object.

## PageLabelScheme
Inherits from a named tuple with fields:
 * `startpage` : Index in the PDF where to start numbering pages according to this scheme
 * `style` : one of the strings `arabic`, `roman uppercase`, `letters uppercase`, `roman lowercase`, `letters lowercase`
 * `prefix` : string to prepend to all page labels
 * `firstpagenum` : where to start the index

## Example

```python
from pdfrw import PdfReader, PdfWriter

from pagelabels import PageLabels, PageLabelScheme

reader = PdfReader("input.pdf")
labels = PageLabels.from_pdf(reader)
newlabel = PageLabelScheme(startpage=3, # the index of the page of the PDF where the labels will start
                           style="roman", # See options in PageLabelScheme.styles()
                           prefix="Appendix ",
                           firstpagenum=1) # number to attribute to the first page of this index
labels.append(newlabel) # Adding our page labels to the existing ones
labels.write(reader)
writer = PdfWriter()
writer.trailer = reader
writer.write("output.pdf")
```