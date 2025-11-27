---
title: Counting Artifacts of a Particular Type in Python via .NET
linktitle: Counting Artifacts
type: docs
weight: 40
url: /python-net/counting-artifacts/
description: This article illustrates how to inspect pagination artifacts in a PDF document using Aspose.PDF for Python via .NET.
lastmod: "2025-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Counting Artifacts in PDF using Python
Abstract: Pagination artifacts such as watermarks, backgrounds, headers, and footers are commonly used in PDF documents to provide structure, branding, and identification. This example demonstrates how to inspect and count these artifacts programmatically using Aspose.PDF for Python via .NET. By filtering artifacts on a page and grouping them by subtype, developers can quickly analyze document composition and verify the presence of specific elements. The provided code illustrates how to open a PDF, extract pagination artifacts from the first page, count each subtype, and output the results, offering a practical approach to document auditing and validation.
---

## Counting Artifacts of a Particular Type

Inspect and count pagination artifacts in a PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) using Aspose.PDF for Python via .NET. Pagination artifacts include elements such as watermarks, backgrounds, headers, and footers that are applied to pages for layout and identification purposes. By filtering [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) objects on a [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) and grouping them by subtype (`Artifact.ArtifactSubtype`), developers can quickly analyze the document's structure and verify the presence of specific elements.

To calculate the total count of artifacts of a particular type (for example, the total number of watermarks), use the following code. The example filters the page's [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) collection (an [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)) by [`Artifact.ArtifactType`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/#properties) and then counts subtypes (`Artifact.ArtifactSubtype`).

1. Open the PDF document (see [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Filter pagination artifacts using the page's [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) collection.
1. Count artifacts by subtype (`Artifact.ArtifactSubtype`).
1. Print results.

```python

import aspose.pdf as ap

def count_pagination_artifacts(path_infile):
    # Open the PDF document
    with ap.Document(path_infile) as document:
        
        # Extract pagination artifacts from the first page
        pagination_artifacts = [
            artifact for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        # Count artifacts by subtype
        watermarks = sum(1 for artifact in pagination_artifacts 
                         if artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK)
        backgrounds = sum(1 for artifact in pagination_artifacts 
                          if artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND)
        headers = sum(1 for artifact in pagination_artifacts 
                      if artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER)
        footers = sum(1 for artifact in pagination_artifacts 
                      if artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER)

        # Display results
        print(f"Watermarks: {watermarks}")
        print(f"Backgrounds: {backgrounds}")
        print(f"Headers: {headers}")
        print(f"Footers: {footers}")
```
