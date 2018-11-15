#!/usr/bin/env python3
from pdfrw import PdfName, PdfDict, PdfArray

from . import PageLabelScheme


class PageLabels(list):
    @classmethod
    def from_pdf(cls, pdf):
        """Create a PageLabels object by reading the page labels of
        the given PdfReader object"""
        labels = pdf.Root.PageLabels
        if not labels:
            return cls([])
        nums = labels.Nums
        parsed = (PageLabelScheme.from_pdf(nums[i], nums[i + 1])
                  for i in range(0, len(nums), 2))
        return cls(parsed)

    def normalize(self, pagenum=float("inf")):
        """Sort the pagelabels, remove duplicate entries,
        and if pegenum is set remove entries that have a startpage >= pagenum"""
        # Remove duplicates
        page_nums = dict()
        for elem in self[:]:
            oldelem = page_nums.get(elem.startpage)
            if oldelem is not None or elem.startpage >= pagenum:
                self.remove(oldelem)
            else:
                page_nums[elem.startpage] = elem
        self.sort()
        if len(self) == 0 or self[0].startpage != 0:
            self.insert(0, PageLabelScheme(0))

    def pdfdict(self):
        """Return a PageLabel entry to pe inserted in the root of a PdfReader object"""
        nums = (i for label in sorted(self)
                for i in label.pdfobjs())
        return PdfDict(Type=PdfName("Catalog"),
                       Nums=PdfArray(nums))

    def write_raw(self, pdf):
        """Write the PageLabels to a PdfReader object without sanity checks
        Use at your own risks, this may corrupt your PDF"""
        pdf.Root.PageLabels = self.pdfdict()

    def write(self, pdf):
        """Write the PageLabels to a PdfReader object, normalizing it first"""
        self.normalize(len(pdf.pages))
        pdf.Root.PageLabels = self.pdfdict()
