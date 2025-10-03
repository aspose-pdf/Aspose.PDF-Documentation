---
title: Convert PDF/x to PDF formats in Python
linktitle: Convert PDF/x to PDF formats
type: docs
weight: 120
url: /python-net/convert-pdf_x-to-pdf/
lastmod: "2025-09-27"
description: This topic shows you how to convert PDF/x to PDF formats using Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: How to convert PDF/x to PDF formats
Abstract: The article provides a comprehensive guide on converting PDF/UA, and PDF/A to PDF file using Aspose.PDF for Python.
---

**PDF/x to PDF format means the ability to convert PDF/UA, and PDF/A to PDF file.**

## Convert PDF/A to PDF

1. Load the PDF document using 'ap.Document'.
1. Call 'remove_pdfa_compliance()' to strip all PDF/A-related compliance settings and metadata.
1. Save the resulting PDF to the output path.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Removing PDF/UA compliance

This function demonstrates a two-step conversion process: first removing PDF/UA (Universal Accessibility) compliance, and then converting the resulting PDF into PDF/A-1B format with automatic tagging for accessibility and semantic structure.

1. Load the PDF document using 'ap.Document()'.
1. Call 'document.remove_pdfa_compliance()' to remove any PDF/A restrictions or compliance settings.
1. Save the modified PDF to 'path_outfile'.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```