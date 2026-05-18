---
title: Seitenversatz abrufen
type: docs
weight: 20
url: /de/python-net/get-page-offset/
description: Dieses Beispiel zeigt, wie man PdfFileInfo verwendet, um die X‑ und Y‑Versätze einer bestimmten Seite zu ermitteln und sie in Zoll umzurechnen, um eine präzise Layout‑ und Positionierungsanalyse durchzuführen.
lastmod: "2026-05-18"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF‑Seitenversätze mit Python abrufen
Abstract: Die Funktion 'get_page_offsets' extrahiert die horizontalen (X) und vertikalen (Y) Versätze jeder Seite in einer PDF‑Datei. Diese Versätze geben die Position des Seiteninhalts relativ zum Ursprung der PDF an. Durch die Umrechnung von Punkten in Zoll liefert die Funktion präzise, menschenlesbare Messwerte, die für die genaue Platzierung von Anmerkungen, Bildern oder Text verwendet werden können. Sie unterstützt mehrseitige PDFs und richtet sich an Entwickler, die an PDF‑Layout, Automatisierung oder Inhaltsausrichtungsaufgaben arbeiten.
---

Die Funktion 'get_page_offsets' liefert Entwicklern die genauen horizontalen (X) und vertikalen (Y) Versätze von Seiten in einer PDF‑Datei. In PDF‑Dokumenten kann jede Seite einen internen Ursprungspunkt haben, der vom oberen linken Eck der Seite abweicht, was die Positionierung von Text, Bildern, Anmerkungen oder anderem Inhalt beeinflussen kann.

Durch die Verwendung von Aspose.PDF Facades extrahiert diese Funktion diese Offsets in Punkt und konvertiert sie in Zoll für eine einfache Interpretation. Sie unterstützt mehrseitige PDFs und ist damit für automatisierte Workflows geeignet, die eine präzise Platzierung von Inhalten erfordern.

1. Erstelle das PDF-Fassade-Objekt.
1. Erhalte die Anzahl der Seiten im PDF.
1. Durchlaufe jede Seite, um die Offsets zu erhalten.
1. Gib die Offsets aus oder speichere sie.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_offsets(infile):
    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_x_offset = pdf_info.get_page_x_offset(1) / 72.0
    page_y_offset = pdf_info.get_page_y_offset(1) / 72.0
    print(f"Page X Offset: {page_x_offset} inches")
    print(f"Page Y Offset: {page_y_offset} inches")
```
