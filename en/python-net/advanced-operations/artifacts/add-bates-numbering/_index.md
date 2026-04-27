---
title: Add Bates Numbering to PDF in Python
linktitle: Adding Bates Numbering
type: docs
weight: 10
url: /python-net/add-bates-numbering/
description: Learn how to add and remove Bates numbering in PDF documents using Python with Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Add Bates Numbering via Python
Abstract: Bates numbering is a critical feature in legal, medical, and business document workflows, ensuring that each page in a set receives a unique, sequential identifier for reliable referencing. This article demonstrates how Aspose.PDF for Python via .NET simplifies the automation of Bates numbering through its flexible API. Using the BatesNArtifact class, developers can configure numbering behavior—including digit count, prefixes, suffixes, alignment, and margins—and apply it programmatically across entire documents. Multiple approaches are presented, from direct artifact application to delegate-based configuration, offering both static and dynamic control. In addition, the API supports complete removal of Bates numbers with a single method call, enabling full lifecycle management of pagination artifacts. Clear, step-by-step code examples illustrate how to add, customize, and delete Bates numbering, making this guide a practical resource for developers seeking to streamline document processing workflows.
---

Bates numbering is widely used in legal, medical, and business workflows to assign unique, sequential identifiers to pages within a document set. Aspose.PDF for Python via .NET offers a simple and flexible API for automating this process, enabling you to apply standardized Bates numbers programmatically across any PDF.

Using the [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) class, developers can fully customize numbering behavior—including the starting number, digit count, prefixes and suffixes, alignment, and margins. Once configured, the artifact can be applied to the [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) through the `add_bates_numbering` method on the [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) or added as part of a list of [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) objects. Aspose.PDF also supports a delegate-based configuration style, allowing for dynamic control of artifact settings at runtime.

In addition to creating Bates numbers, the API provides an easy way to remove them using `delete_bates_numbering`, offering complete flexibility in document processing workflows.

This article shows multiple methods for adding and removing Bates numbering in a PDF using Aspose.PDF for Python via .NET, with clear examples of artifact configuration, application, and removal.

## Adding Bates Numbering Artifact

This example shows how to programmatically add Bates numbering to a PDF document using Aspose.PDF for Python via .NET. By configuring a [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) with the desired settings and applying it to the document's pages, you can automate the process of adding standardized identifiers to each page.

To add a Bates-numbering artifact to a [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), call the `AddBatesNumbering(BatesNArtifact)` extension method on the [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), passing a [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) instance as the parameter:

```python
import sys
from os import path
import aspose.pdf as ap

def _create_bates_artifact():
    """Create a Bates numbering artifact with default settings."""
    artifact = ap.BatesNArtifact()
    artifact.start_page = 1
    artifact.end_page = 0
    artifact.subset = ap.Subset.ALL
    artifact.number_of_digits = 6
    artifact.start_number = 1
    artifact.prefix = ""
    artifact.suffix = ""
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
    artifact.right_margin = 72
    artifact.left_margin = 72
    artifact.top_margin = 36
    artifact.bottom_margin = 36
    return artifact
```

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## Add Bates Numbering Using Pagination Artifacts

Add Bates numbering to a PDF using the pagination artifacts collection in Aspose.PDF for Python:

1. Load the PDF document.
1. Insert extra pages if needed before applying numbering.
1. Create a Bates artifact.
1. Configure artifact properties.
1. Add the artifact to pagination collection.
1. Apply pagination to pages.
1. Save the updated document.

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## Delete Bates Numbering

To remove Bates numbering from a [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), use the `delete_bates_numbering()` method on the [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python
import sys
from os import path
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## Related Artifact Topics

- [Work with PDF artifacts in Python](/pdf/python-net/artifacts/)
- [Add watermarks to PDF in Python](/pdf/python-net/add-watermarks/)
- [Add PDF backgrounds in Python](/pdf/python-net/add-backgrounds/)
- [Count artifact types in PDF files](/pdf/python-net/counting-artifacts/)