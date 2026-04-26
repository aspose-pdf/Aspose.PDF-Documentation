---
title: Usage Rights Management
type: docs
weight: 100
url: /python-net/usage-rights-management/
description: Learn how to detect and remove usage rights from PDF documents using PdfFileSignature in Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Remove PDF Usage Rights in Python
Abstract: This article explains how to inspect and remove usage rights from PDF documents with Aspose.PDF for Python via .NET. It shows how to check whether a PDF contains usage rights and how to save a new version of the document after those rights are removed.
---

Aspose.PDF for Python via .NET provides the [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) facade for working with signed PDFs and related usage-rights settings. In some workflows, you may need to inspect whether a document contains usage rights and remove them before saving an updated version of the file.

This example demonstrates one common usage-rights management task:

1. Check whether a PDF contains usage rights.
1. Remove usage rights from the document.
1. Save the updated PDF file.

## Check whether the PDF contains usage rights

Before removing usage rights, the example checks the current state of the document by calling `contains_usage_rights()`. This lets you confirm whether usage rights are present before making changes.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_usage_rights(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights: {had_usage_rights}")
    finally:
        pdf_signature.close()
```

## Remove usage rights from the PDF

Use `remove_usage_rights()` when the document should no longer retain its existing usage-rights settings. The example checks the initial state, removes the rights, and saves the updated PDF to a new file.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_usage_rights(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights before removal: {had_usage_rights}")
        pdf_signature.remove_usage_rights()
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
