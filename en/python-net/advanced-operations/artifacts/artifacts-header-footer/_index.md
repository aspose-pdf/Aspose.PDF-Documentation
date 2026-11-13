---
title: Add PDF Headers and Footers in Python
linktitle: Add Headers and Footers
type: docs
weight: 70
url: /python-net/artifacts-header-footer/
description: Add styled header and footer artifacts to PDF pages in Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Headers and Footers in a PDF with Python
Abstract: Add styled header and footer artifacts to PDF pages in Python.
---

Use `HeaderArtifact` and `FooterArtifact` to add running text to PDF pages. These examples add artifacts to the first page.

## Create Styled Text Artifacts

Define this helper before running either add example. It applies the same font, size, color, and alignment to headers and footers.

```python
import aspose.pdf as ap

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

Pass `HeaderArtifact` to the helper and append the result to the page.

```python
import aspose.pdf as ap

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## Add Footer to PDF

Pass `FooterArtifact` to the helper and append the result to the page.

```python
import aspose.pdf as ap

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## Related Artifact Topics

- [Remove Headers and Footers](/pdf/python-net/remove-headers-footers/)
- [Work with PDF artifacts in Python](/pdf/python-net/artifacts/)
