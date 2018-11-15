#!/usr/bin/env python3
from collections import namedtuple

from pdfrw import PdfName, PdfDict, PdfObject, PdfString

PageLabelTuple = namedtuple("PageLabelScheme",
                            "startpage style prefix firstpagenum")

defaults = {"style": "arabic", "prefix": '', "firstpagenum": 1}
styles = {"arabic": PdfName('D'),
          "roman lowercase": PdfName('r'),
          "roman uppercase": PdfName('R'),
          "letters lowercase": PdfName('a'),
          "letters uppercase": PdfName('A')}
stylecodes = {v: a for a, v in styles.items()}


class PageLabelScheme(PageLabelTuple):
    """Represents a page numbering scheme.
        startpage : the index in the pdf (starting from 0) of the
                    first page the scheme will be applied to.
        style : page numbering style (arabic, roman [lowercase|uppercase], letters [lowercase|uppercase])
        prefix: a prefix to be prepended to all page labels
        firstpagenum : where to start numbering
    """
    __slots__ = tuple()

    def __new__(cls, startpage,
                style=defaults["style"],
                prefix=defaults["prefix"],
                firstpagenum=defaults["firstpagenum"]):
        if style not in styles:
            raise ValueError("PageLabel style must be one of %s" % cls.styles())
        return super().__new__(cls, int(startpage), style, str(prefix), int(firstpagenum))

    @classmethod
    def from_pdf(cls, pagenum, opts):
        """Returns a new PageLabel using options from a pdfrw object"""
        return cls(pagenum,
                   style=stylecodes.get(opts.S, defaults["style"]),
                   prefix=(opts.P and opts.P.decode() or defaults["prefix"]),
                   firstpagenum=(opts.St or defaults["firstpagenum"]))

    @staticmethod
    def styles():
        """List of the allowed styles"""
        return styles.keys()

    def pdfobjs(self):
        """Returns a tuple of two elements to insert in the PageLabels.Nums
        entry of a pdf"""
        page_num = PdfObject(self.startpage)
        opts = PdfDict(S=styles[self.style])
        if self.prefix != defaults["prefix"]:
            opts.P = PdfString.encode(self.prefix)
        if self.firstpagenum != defaults["firstpagenum"]:
            opts.St = PdfObject(self.firstpagenum)
        return page_num, opts
