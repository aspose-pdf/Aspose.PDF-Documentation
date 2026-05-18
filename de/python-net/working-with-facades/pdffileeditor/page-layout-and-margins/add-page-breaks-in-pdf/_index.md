---
title: Seitenumbrüche in PDF hinzufügen
type: docs
weight: 20
url: /de/python-net/add-page-breaks-in-pdf/
description: Fügen Sie Seitenumbrüche in ein PDF-Dokument mit Aspose.PDF for Python ein.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Seitenumbrüche programmatisch zu PDF-Seiten in Python hinzufügen
Abstract: Erfahren Sie, wie Sie mit Aspose.PDF for Python Seitenumbrüche in ein PDF-Dokument einfügen. Dieses Beispiel zeigt, wie man eine Seite an einer angegebenen vertikalen Position aufteilt, sodass Entwickler Inhalte neu anordnen und dynamisch zusätzliche Seiten erstellen können.
---

Seitenumbrüche sind nützlich, wenn Sie lange PDF-Seiten in mehrere Seiten aufteilen oder steuern müssen, wie Inhalte über ein Dokument verteilt werden. Mit Aspose.PDF for Python können Entwickler Seitenumbrüche an bestimmten Positionen einfügen, ohne das PDF manuell zu bearbeiten.

Dieser Artikel zeigt, wie die Methode 'add_page_break' verwendet wird [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) Klasse, um einen Seitenumbruch an einer definierten vertikalen Koordinate auf einer ausgewählten Seite einzufügen. Die Methode erstellt eine neue Seite und verschiebt den Inhalt unterhalb des Umbruchpunkts auf diese Seite.

1. Erstelle ein PdfFileEditor-Objekt.
1. Definiere die Position des Seitenumbruchs.
1. Füge den Seitenumbruch ein.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Page Breaks in PDF
def add_page_breaks_in_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.add_page_break(
        infile,
        outfile,
        [
            pdf_facades.PdfFileEditor.PageBreak(1, 400),
        ],
    )
```
