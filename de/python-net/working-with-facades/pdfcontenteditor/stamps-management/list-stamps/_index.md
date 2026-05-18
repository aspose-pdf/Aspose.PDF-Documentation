---
title: Stempel auflisten
type: docs
weight: 70
url: /de/python-net/list-stamps/
description: Dieses Beispiel lädt ein PDF, ruft alle Stempel von Seite 1 ab, gibt sie aus und zeigt eine Meldung an, wenn keine Stempel gefunden werden.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rubber-Stempel-Anmerkungen in einem PDF mit PdfContentEditor in Python auflisten
Abstract: Dieses Beispiel zeigt, wie man Rubber-Stempel-Anmerkungen aus einem PDF‑Dokument mit Aspose.PDF for Python via the Facades API abruft und auflistet. Es demonstriert, wie man auf Stempel einer bestimmten Seite zugreift und deren Details anzeigt.
---

Beim Arbeiten mit annotierten PDFs muss man möglicherweise vorhandene Rubber-Stempel prüfen, bevor man sie ändert oder entfernt. Die Methode 'get_stamps()' ermöglicht das Abrufen aller auf einer bestimmten Seite platzierten Stempel. Anschließend kann man die Ergebnisse durchlaufen und programmgesteuert verarbeiten.

1. Erstelle ein [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Alle Stempel von Seite 1 abrufen.
1. Iterieren Sie durch die Stempelsammlung.
1. Geben Sie jeden Stempel aus.
1. Zeigen Sie eine Meldung an, wenn keine Stempel vorhanden sind.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def list_stamps(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # List all stamps on page 1
    stamps = content_editor.get_stamps(1)

    count = 0
    for stamp in stamps:
        count += 1
        print(f"Stamp {count}: {stamp}")

    if count == 0:
        print("No stamps found")
```
