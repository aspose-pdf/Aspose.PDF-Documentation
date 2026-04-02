---
title: Revision and Permissions
type: docs
weight: 40
url: /python-net/revision-permissions/
description: Learn how to inspect signature revisions, document revisions, and certification permissions in PDF files using PdfFileSignature in Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Read PDF Signature Revision and Access Permission Data in Python
Abstract: This article explains how to inspect revision and permission information in signed or certified PDF files with Aspose.PDF for Python via .NET. It shows how to get the revision number of a signature, count total document revisions, and read access permissions from a certified PDF.
---

Aspose.PDF for Python via .NET provides the [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) facade for working with signed and certified PDF documents. Besides adding signatures, you can also inspect signature metadata to understand how many revisions a document contains and what changes are allowed after certification.

This example demonstrates three common inspection tasks:

1. Get the revision number for an existing signature.
1. Get the total number of revisions in a signed document.
1. Read the access permissions from a certified PDF.

## Get the revision number for a signature

Use this approach when a PDF already contains one or more signatures and you need to identify the revision associated with a specific signature. The example resolves the first available signature name and then calls `get_revision()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

def get_signature_revision(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_revision = pdf_signature.get_revision(sign_name)
        print(f"Signature Revision for '{sign_name}': {signature_revision}")
    finally:
        pdf_signature.close()
```

## Get the total number of document revisions

Use `get_total_revision()` when you need to know how many revisions are stored in the signed PDF. This is useful for checking whether the document has gone through multiple updates after the original signature was applied.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

def get_total_document_revisions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        total_revisions = pdf_signature.get_total_revision()
        print(f"Total Document Revisions: {total_revisions}")
    finally:
        pdf_signature.close()
```

## Get access permissions from a certified PDF

Certified documents can define what changes are allowed after certification. Use `get_access_permissions()` to inspect that permission level and determine whether the document allows no changes, form filling, or other controlled modifications.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

def get_access_permissions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        access_permissions = pdf_signature.get_access_permissions()
        print(f"Access Permissions: {access_permissions}")
    finally:
        pdf_signature.close()
```

