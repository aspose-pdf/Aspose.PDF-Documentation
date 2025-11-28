---
title: Adding Bates Numbering Artifact in Python via .NET
linktitle: Adding Bates Numbering
type: docs
weight: 10
url: /python-net/add-bates-numbering/
description: Aspose.PDF for Python via .NET allows you to add Bates Numbering to PDF.
lastmod: "2025-11-13"
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

import aspose.pdf as ap

def add_bates_numbering(path_outfile):
    # Create a new or empty PDF document
    with ap.Document() as document:

        # Add 10 blank pages
        for _ in range(10):
            document.pages.add()

        # Create Bates numbering artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,  # 0 = apply until last page
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add Bates numbering to all pages
        document.pages.add_bates_numbering(bates)

        # Save the resulting PDF
        document.save(path_outfile)
```

Or, you can pass a collection of [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) objects:

```python

import aspose.pdf as ap

def add_bates_numbering_collection(path_outfile):
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Create Bates artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add as a pagination artifact list
        document.pages.add_pagination([bates])

        # Save document
        document.save(path_outfile)
```

Add a Bates numbering artifact using an action delegate:

```python

import aspose.pdf as ap

def add_bates_numbering_delegate(path_outfile):
    def configure_bates(b):
        """Configure Bates numbering artifact with desired settings."""
        b.start_page = 1
        b.end_page = 0
        b.subset = ap.Subset.ALL
        b.number_of_digits = 6
        b.start_number = 1
        b.prefix = ""
        b.suffix = ""
        b.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
        b.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
        b.right_margin = 72
        b.left_margin = 72
        b.top_margin = 36
        b.bottom_margin = 36
        b.text_state.font_size = 10
    
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Use delegate function to configure Bates artifact
        document.pages.add_bates_numbering(configure_bates)

        # Save output PDF
        document.save(path_outfile)
```

## Delete Bates Numbering

To remove Bates numbering from a [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), use the `delete_bates_numbering()` method on the [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python

import aspose.pdf as ap

def delete_bates_numbering(path_infile, path_outfile):
    with ap.Document(path_infile) as document:

        # Remove Bates numbering from all pages
        document.pages.delete_bates_numbering()

        # Save updated document
        document.save(path_outfile)
```