---
title: Manage PDF Headers and Footers using Python
linktitle: Manage PDF Headers and Footers
type: docs
weight: 70
url: /python-net/artifacts-header-footer/
description: Learn how to manage headers and footers in PDF documents with Python and Aspose.PDF.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to Add, Customize, and Remove PDF Headers and Footers Using Python
Abstract: Managing headers and footers is a common requirement when working with PDF documents in business, publishing, and automation workflows. This article demonstrates how to use Aspose.PDF for Python to add professional-looking headers and footers with custom styling such as font, size, color, and alignment. It also shows how to detect and remove existing pagination artifacts like headers and footers from a PDF page. With reusable functions and clear examples, developers can quickly integrate these features into document processing systems for branding, reporting, or file cleanup.
---

## Create Styled Text Artifacts

This utility function explains how to create a reusable text artifact for PDF pages using Aspose.PDF for Python. It is designed for generating styled headers or footers with consistent formatting, including font settings, color, size, and alignment. The function abstracts artifact creation so it can be reused for different page-level text decorations.

1. Instantiate the artifact object.
1. Set artifact text content.
1. Apply text styling.
1. Set alignment.
1. Return configured artifact.

```python
from os import path
import aspose.pdf as ap
import sys

def _create_text_artifact(artifact_class, text):
    """Create a text artifact (header/footer) with common styling."""
    artifact = artifact_class()
    artifact.text = text
    artifact.text_state.font_size = 14
    artifact.text_state.font = ap.text.FontRepository.find_font("Arial")
    artifact.text_state.foreground_color = ap.Color.navy
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    return artifact

```

## Add Header to PDF

1. Open the input PDF.
1. Create a HeaderArtifact with text "Sample Header".
1. Append it to the first page.
1. Save the updated PDF.

```python
from os import path
import aspose.pdf as ap
import sys

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## Add Footer to PDF

1. Open the input PDF.
1. Create a FooterArtifact with text "Sample Footer".
1. Append it to the first page.
1. Save the output file.

```python
from os import path
import aspose.pdf as ap
import sys

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## Delete Header or Footer Artifacts

1. Open the PDF.
1. Find artifacts marked as pagination headers or footers.
1. Remove them from the first page.
1. Save the cleaned document.

```python
from os import path
import aspose.pdf as ap
import sys

def delete_header_footer_artifact(infile, outfile):
    with ap.Document(infile) as document:
        header_footers = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and (
                artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER
                or artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER
            )
        ]

        for art in header_footers:
            document.pages[1].artifacts.delete(art)

        document.save(outfile)
```