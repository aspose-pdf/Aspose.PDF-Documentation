---
title: PDF-Seiteninhalt skalieren
type: docs
weight: 30
url: /de/python-net/resize-pdf-page-contents/
description: Skalieren Sie den Inhalt bestimmter PDF-Seiten mit Aspose.PDF für Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Seiteninhalt programmgesteuert in Python skalieren
Abstract: Erfahren Sie, wie Sie den Inhalt bestimmter PDF-Seiten mit Aspose.PDF für Python skalieren können. Dieses Beispiel zeigt, wie Sie Breite und Höhe des Seiteninhalts anpassen, während Sie die Dokumentstruktur beibehalten, um Layouts für den Druck oder die Anzeige leichter zu optimieren.
---

Die Anpassung der Größe von PDF-Seiteninhalten ist oft notwendig, wenn Dokumente für den Druck vorbereitet, Inhalte in ein bestimmtes Layout eingefügt oder Seitenformate über ein Dokument hinweg standardisiert werden sollen. Mit Aspose.PDF für Python können Entwickler die Inhalte ausgewählter Seiten programmgesteuert skalieren, ohne das Dokument manuell zu bearbeiten.

Dieser Artikel zeigt, wie man die 'resize_contents'-Methode von [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) Klasse zum Ändern der Abmessungen des Seiteninhalts für bestimmte Seiten in einer PDF-Datei. Durch Angabe der Zielbreite und -höhe wird der Inhalt auf den ausgewählten Seiten entsprechend skaliert.

1. Erstelle ein PdfFileEditor-Objekt.
1. Seiteninhalt skalieren.

Parameter:

- [1, 3] – Liste der Seitenzahlen, deren Inhalte skaliert werden.
- 400 – die neue Breite des Seiteninhalts (in Punkten).
- 750 – die neue Höhe des Seiteninhalts (in Punkten).

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resize PDF Page Contents
def resize_pdf_page_contents(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    if not pdf_editor.resize_contents(
        FileIO(infile), FileIO(outfile, "w"), [1, 3], 400, 750
    ):
        raise Exception("Failed to resize PDF page contents.")
```
