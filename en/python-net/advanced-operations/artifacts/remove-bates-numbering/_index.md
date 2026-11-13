---
title: Remove PDF Bates Numbering in Python
linktitle: Remove Bates Numbering
type: docs
weight: 100
url: /python-net/remove-bates-numbering/
description: Remove Bates numbering from all pages of a PDF in Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove Bates Numbering in a PDF with Python
Abstract: Remove Bates numbering from all pages of a PDF in Python.
---

Remove Bates numbering from all pages of a PDF in Python.

## Delete Bates numbering

Pass the document’s pages to `PageCollectionExtensions.delete_bates_numbering` and save the PDF.

```python
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## Related Artifact Topics

- [Add Bates Numbering](/pdf/python-net/add-bates-numbering/)
- [Work with PDF artifacts in Python](/pdf/python-net/artifacts/)
