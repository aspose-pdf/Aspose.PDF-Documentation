---
title: Seiten zu PDF hinzufügen
type: docs
weight: 10
url: /de/python-net/append-pages-to-pdf/
description: Fügen Sie Seiten von einem PDF-Dokument zu einem anderen hinzu, indem Sie Aspose.PDF for Python verwenden.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Seiten von einem PDF zu einem anderen in Python anhängen
Abstract: Erfahren Sie, wie Sie Seiten von einem PDF-Dokument zu einem anderen hinzufügen, indem Sie Aspose.PDF for Python verwenden. Dieses Beispiel zeigt, wie die Klasse PdfFileEditor verwendet wird, um Seiten aus mehreren PDFs zu kombinieren und ein einziges Ausgabedokument zu erstellen.
---

Das Kombinieren von Seiten aus verschiedenen PDF-Dokumenten ist eine häufige Anforderung in Dokumentenverarbeitungs-Workflows. Mit Aspose.PDF for Python können Entwickler problemlos Seiten von einer oder mehreren PDF-Dateien zu einem bestehenden Dokument hinzufügen.

Dieses Code‑Snippet zeigt, wie die append‑Methode der [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) Klasse, um ausgewählte Seiten aus einer anderen PDF-Datei an das Ende einer Quell-PDF anzufügen. Durch die Angabe des Seitenbereichs können Entwickler genau steuern, welche Seiten im endgültigen Dokument enthalten sind.

1. Erstelle ein PdfFileEditor-Objekt.
1. Seiten aus einer anderen PDF anhängen.

Die angegebenen Seiten aus dem sekundären PDF-Dokument werden an das Ende des ursprünglichen PDFs angehängt, wodurch eine kombinierte Ausgabedatei entsteht.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Append Pages to PDF
def append_pages_to_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Append pages from the specified PDF document to the end of the source PDF document
    pdf_editor.append(infile, [sample_file], 1, 2, outfile)
```
