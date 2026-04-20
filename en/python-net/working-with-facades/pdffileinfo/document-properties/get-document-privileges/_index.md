---
title: Get Document Privileges
type: docs
weight: 10
url: /python-net/get-document-privileges/
description: Learn how to programmatically check the privileges of a PDF document using Aspose.PDF for Python. This tutorial demonstrates how to use the PdfFileInfo class to read the document’s security settings, such as printing, copying, or modifying permissions.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Retrieve PDF Document Privileges Using Aspose.PDF for Python
Abstract: PDF documents can have security restrictions that limit actions like printing, copying, modifying, or filling forms. By accessing these privileges programmatically, developers can determine what operations are allowed on a PDF. This guide shows how to use the PdfFileInfo class to retrieve a PDF’s document privileges and display them in Python.    
---

PDF privileges control what users can and cannot do with a document. Common permissions include:

- Printing the document
- Copying content
- Modifying annotations or contents
- Filling form fields
- Using screen readers
- Assembling or merging documents

With Aspose.PDF for Python, you can inspect these settings programmatically using the [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) class. This is especially useful when working with multiple PDFs in automated workflows, verifying compliance, or controlling document handling in applications.

1. Load a PDF file.
1. Retrieve its document privileges.
1. Display which actions are allowed for the document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_document_privileges(input_file_name):
    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)

    privileges = pdf_metadata.get_document_privilege()

    print("Document Privileges:")
    print(f"  Can Print: {privileges.allow_print}")
    print(f"  Can Degraded Print: {privileges.allow_degraded_printing}")
    print(f"  Can Copy: {privileges.allow_copy}")
    print(f"  Can Modify Contents: {privileges.allow_modify_contents}")
    print(f"  Can Modify Annotations: {privileges.allow_modify_annotations}")
    print(f"  Can Fill In: {privileges.allow_fill_in}")
    print(f"  Can Screen Readers: {privileges.allow_screen_readers}")
    print(f"  Can Assembly: {privileges.allow_assembly}")
```
