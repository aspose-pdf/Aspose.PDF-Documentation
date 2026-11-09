---
title: Add Watermarks to PDF in Python
linktitle: Add Watermarks
type: docs
weight: 30
url: /python-net/add-watermarks/
description: Add styled text watermark artifacts to PDF pages in Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Watermarks in a PDF with Python
Abstract: Add styled text watermark artifacts to PDF pages in Python.
---

Use `WatermarkArtifact` to add a text watermark to the first page of a PDF.

## Add a Watermark to PDF

Set the text and style, then configure alignment, rotation, and opacity. Set `is_background` to place the watermark behind page content.

```python
import aspose.pdf as ap

def add_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        text_state = ap.text.TextState()
        text_state.font_size = 72
        text_state.foreground_color = ap.Color.blue_violet
        text_state.font_style = ap.text.FontStyles.BOLD
        text_state.font = ap.text.FontRepository.find_font("Arial")

        watermark = ap.WatermarkArtifact()
        watermark.set_text_and_state("WATERMARK", text_state)
        watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
        watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
        watermark.rotation = 60
        watermark.opacity = 0.2
        watermark.is_background = True

        document.pages[1].artifacts.append(watermark)
        document.save(outfile)
```

## Related Artifact Topics

- [Extract Watermark Details](/pdf/python-net/extract-watermarks/)
- [Remove Watermarks](/pdf/python-net/remove-watermarks/)
- [Work with PDF artifacts in Python](/pdf/python-net/artifacts/)
