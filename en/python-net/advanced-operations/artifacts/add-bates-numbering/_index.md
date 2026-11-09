---
title: Add Bates Numbering to PDF in Python
linktitle: Add Bates Numbering
type: docs
weight: 10
url: /python-net/add-bates-numbering/
description: Add sequential Bates identifiers to PDF pages in Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Bates Numbering in a PDF with Python
Abstract: Add sequential Bates identifiers to PDF pages in Python.
---

Bates numbering assigns sequential identifiers to pages in a document set. Configure a `BatesNArtifact` to control the page range, starting number, digit count, prefix, suffix, and placement.

## Adding Bates Numbering Artifact

Pass the configured artifact and the document’s pages to `PageCollectionExtensions.add_bates_numbering`. This example applies six-digit identifiers starting at `000001` to the existing pages.

```python
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


def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## Add Bates Numbering Using Pagination Artifacts

To apply Bates numbering through the pagination API, reuse `_create_bates_artifact` from the previous example and pass the artifact in a list to `PageCollectionExtensions.add_pagination`.

```python
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## Related Artifact Topics

- [Remove Bates Numbering](/pdf/python-net/remove-bates-numbering/)
- [Work with PDF artifacts in Python](/pdf/python-net/artifacts/)
