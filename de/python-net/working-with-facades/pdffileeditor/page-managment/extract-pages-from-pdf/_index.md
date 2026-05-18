---
title: Seiten aus PDF extrahieren
type: docs
weight: 30
url: /de/python-net/extract-pages-from-pdf/
description: Ausgewählte Seiten aus einem PDF‑Dokument mit Aspose.PDF für Python extrahieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Spezifische Seiten aus einem PDF‑Dokument in Python extrahieren
Abstract: Erfahren Sie, wie Sie ausgewählte Seiten aus einem PDF‑Dokument mit Aspose.PDF für Python extrahieren. Dieses Beispiel zeigt, wie ein neues PDF erstellt wird, das nur die benötigten Seiten enthält, und ermöglicht die Erstellung benutzerdefinierter Dokumente sowie die seitenbezogene Manipulation.
---

Das Extrahieren von Seiten aus einem PDF ist nützlich, wenn Sie eine Teilmenge eines Dokuments erstellen, nur bestimmte Inhalte teilen oder PDFs für Präsentationen, Berichte oder den Druck neu organisieren müssen. Mit Aspose.PDF für Python können Entwickler programmgesteuert Seiten aus einer PDF‑Datei extrahieren und als neues Dokument speichern.

Erfahren Sie, wie Sie die extract‑Methode von [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) Klasse. Durch die Angabe einer Liste von zu extrahierenden Seiten können Sie ein neues PDF erzeugen, das nur die ausgewählten Seiten enthält, während der ursprüngliche Inhalt und die Formatierung beibehalten werden.

1. Erstelle ein PdfFileEditor-Objekt.
1. Seiten zum Extrahieren definieren.
1. Seiten extrahieren.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Extract Pages from PDF
def extract_pages_from_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page numbers to be extracted (1-based index)
    pages_to_extract = [1, 4, 3]

    # Extract the specified pages from the PDF document and save to a new PDF document
    pdf_editor.extract(infile, pages_to_extract, outfile)
```
