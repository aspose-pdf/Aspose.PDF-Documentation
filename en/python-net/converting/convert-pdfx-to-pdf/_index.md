---
title: Convert PDF/A and PDF/UA to PDF in Python
linktitle: Convert PDF/x to PDF formats
type: docs
weight: 120
url: /python-net/convert-pdf_x-to-pdf/
lastmod: "2026-04-14"
description: Learn how to remove PDF/A and PDF/UA compliance from PDF files in Python with Aspose.PDF for Python via .NET and save them as standard PDF documents.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: How to convert PDF/A and PDF/UA to standard PDF in Python
Abstract: This article explains how to remove PDF/A and PDF/UA compliance from standards-based PDF documents using Aspose.PDF for Python via .NET. It covers scenarios where you may need a standard PDF instead of an archival or accessibility-constrained file, and shows how to save the result after removing compliance metadata and restrictions.
---

Use this page when you need to convert a standards-based PDF, such as PDF/A or PDF/UA, back into a regular PDF document for downstream editing, processing, or redistribution.

Standards-compliant PDFs are helpful for archival, print, and accessibility workflows, but in some cases you may need to remove that compliance before integrating the file into other systems or pipelines. Aspose.PDF for Python via .NET lets you do that programmatically and then save the result as a standard PDF file.

## Convert PDF/A to PDF

This example removes PDF/A compliance metadata and restrictions from a PDF so that the document can be saved as a regular PDF file again.

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

This example demonstrates how to remove PDF/UA-related compliance so the document can be saved as a standard PDF for non-accessibility-specific workflows.

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

## When to use this workflow

- Remove compliance settings before sending a document into a toolchain that does not require PDF/A or PDF/UA restrictions.
- Simplify downstream document processing when archival or accessibility metadata is no longer needed.
- Normalize input PDFs before exporting them to other formats.

## Related conversions

- [Convert PDF to PDF/A, PDF/E, and PDF/X](/pdf/python-net/convert-pdf-to-pdf_x/) if you need the opposite workflow and want to create standards-compliant PDFs.
- [Convert PDF to Word](/pdf/python-net/convert-pdf-to-word/) for editable document output after removing compliance constraints.
- [Convert PDF to HTML](/pdf/python-net/convert-pdf-to-html/) for browser-friendly output from standard PDF files.
