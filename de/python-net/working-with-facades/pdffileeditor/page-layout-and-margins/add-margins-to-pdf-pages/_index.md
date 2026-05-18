---
title: Ränder zu PDF-Seiten hinzufügen
type: docs
weight: 10
url: /de/python-net/add-margins-to-pdf-pages/
description: Fügen Sie benutzerdefinierte Ränder zu ausgewählten Seiten eines PDF mit Aspose.PDF für Python hinzu.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Benutzerdefinierte Ränder zu bestimmten PDF-Seiten in Python hinzufügen
Abstract: Erfahren Sie, wie Sie benutzerdefinierte Ränder zu ausgewählten Seiten eines PDF mit Aspose.PDF für Python hinzufügen. Dieses Beispiel zeigt, wie Sie Seitenränder erweitern, indem Sie oben, unten, links und rechts Ränder für einzelne Seiten festlegen, wodurch PDFs besser druckbar oder visuell konsistent werden.
---

Das Hinzufügen von Rändern zu PDF-Seiten kann die Lesbarkeit verbessern, Dokumente für den Druck vorbereiten oder Platz für Anmerkungen schaffen. Mit Aspose.PDF für Python können Entwickler programmgesteuert Ränder zu bestimmten Seiten eines PDF hinzufügen, ohne das Layout des Inhalts zu ändern.

In diesem Code‑Snippet, die [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) Klasse wird verwendet, um 0,5‑Zoll‑Ränder zu den Seiten 1 und 3 des Eingabedokuments hinzuzufügen. Die Ränder werden in Punkten definiert (1 Zoll = 72 Punkte) und einzeln auf links, rechts, oben und unten jeder Seite angewendet.

1. Öffnen Sie das Quell‑PDF‑Dokument.
1. Erstellen Sie eine 'PdfFileEditor'-Instanz.
1. Definieren Sie die Ränder und die zu ändernden Seiten.
1. Wenden Sie die Ränder mit der Methode 'add_margins' an.
1. Speichern Sie das aktualisierte PDF in die Ausgabedatei.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Margins to PDF Pages
def add_margins_to_pdf_pages(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Define the margins to be added (in points)
    left_margin = 36  # 0.5 inch
    right_margin = 36  # 0.5 inch
    top_margin = 36  # 0.5 inch
    bottom_margin = 36  # 0.5 inch

    pdf_editor.add_margins(
        infile, outfile, [1, 3], left_margin, right_margin, top_margin, bottom_margin
    )
```
