---
title: Stempel nach ID verwalten
type: docs
weight: 95
url: /de/python-net/manage-stamp-by-id/
description: Wie man Gummistempel‑Anmerkungen in einem PDF anhand ihrer eindeutigen IDs mit Aspose.PDF für Python manipuliert
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Verwalte Gummistempel nach ID in einem PDF mit PdfContentEditor in Python
Abstract: Dieses Beispiel demonstriert, wie man Gummistempel‑Anmerkungen in einem PDF anhand ihrer eindeutigen IDs mit Aspose.PDF für Python über die Facades‑API manipuliert. Sie können bestimmte Stempel auf bestimmten Seiten ausblenden oder einblenden, ohne andere Stempel zu beeinflussen.
---

In PDFs mit mehreren Gummistempeln kann es nützlich sein, einzelne Stempel basierend auf ihrer ID zu steuern. Die Methoden 'hide_stamp_by_id()' und 'show_stamp_by_id()' ermöglichen eine selektive Sichtbarkeitskontrolle. Dieses Beispiel zeigt, wie man:

- Mehrere Stempel mit eindeutigen IDs hinzufügen
- Stempel auf einer bestimmten Seite ausblenden
- Stempel auf einer anderen Seite einblenden

Durch die Verwendung von ID-basierten Operationen vermeiden Sie das Verfolgen von Stempeln nach Seitenposition oder anderen Attributen.

1. Erstelle ein [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Fügen Sie Gummistempel mit spezifischen IDs hinzu.
1. Stempel basierend auf ihren IDs und Seitenzahlen verstecken und anzeigen.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def manage_stamp_by_id(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(200, 380, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 480, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    # Apply ID-based stamp operations
    content_editor.hide_stamp_by_id(1, 1)
    content_editor.show_stamp_by_id(1, 2)

    # Save updated document
    content_editor.save(outfile)
```
