---
title: Import and Export Annotations using Python
linktitle: Import and Export Annotations
type: docs
weight: 80
url: /python-net/import-export-annotations/
description: Learn how to import annotations from one PDF and export them into a new PDF document using Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Transfer PDF annotations between documents in Python.
Abstract: This article explains how to copy annotations from a source PDF and export them into a new PDF document using Aspose.PDF for Python via .NET. The walkthrough breaks the process into small steps, including loading the source file, creating the destination document, adding a page, copying annotations from the first page, and saving the result.
---

This article shows how to import annotations from an existing PDF and export them to a new PDF document using Aspose.PDF for Python via .NET.

The example reads annotations from the first page of a source file, creates a new PDF, adds a blank page, and copies each annotation to that new page. This approach is useful when you need to move comments, markup, or review notes into a separate output document.

## Load the source PDF

Create a `Document` object for the input file that already contains annotations. This object gives access to the pages collection and the annotations stored on each page.

```python
source_document = ap.Document(infile)
```

## Create the destination PDF

Next, create an empty PDF document that will receive the imported annotations. At this stage, the destination document does not contain any pages.

```python
destination_document = ap.Document()
```

## Add a page for exported annotations

Because annotations must belong to a page, add a new page to the destination document before copying anything.

```python
page = destination_document.pages.add()
```

## Copy annotations from the source page

Iterate through the annotations collection on the first page of the source PDF and add each annotation to the new page in the destination document.

The second argument in `page.annotations.add(annot, True)` tells Aspose.PDF to copy the annotation into the destination page instead of only reusing the existing object reference.

```python
for annot in source_document.pages[1].annotations:
    page.annotations.add(annot, True)
```

## Save the output document

After all annotations have been copied, save the destination document to create the final PDF file.

```python
destination_document.save(outfile)
```

## Complete example

The following code combines all the steps into one reusable function:

```python
import sys
import aspose.pdf as ap
from os import path


sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def import_export(infile, outfile):
    """
    Import annotations from one PDF document and export them to a new PDF document.
    """
    source_document = ap.Document(infile)
    destination_document = ap.Document()

    page = destination_document.pages.add()

    for annot in source_document.pages[1].annotations:
        page.annotations.add(annot, True)

    destination_document.save(outfile)
```

## Related Topics

- [Interactive Annotations](/python-net/interactive-annotations/)
- [Markup Annotations](/python-net/markup-annotations/)
- [Media Annotations](/python-net/media-annotations/)
- [Security Annotations](/python-net/security-annotations/)
- [Shape Annotations](/python-net/shape-annotations/)
- [Text Based Annotations](/python-net/text-based-Annotations/)
- [Watermark Annotations](/python-net/watermark-annotations/)
