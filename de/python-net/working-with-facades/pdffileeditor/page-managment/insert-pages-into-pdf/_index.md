---
title: Seiten in PDF einfügen
type: docs
weight: 40
url: /de/python-net/insert-pages-into-pdf/
description: Seiten aus einem PDF in ein anderes einfügen mit Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Seiten aus einem anderen PDF in ein bestehendes PDF in Python einfügen
Abstract: Erfahren Sie, wie Sie Seiten aus einem PDF in ein anderes mit Aspose.PDF for Python einfügen. Dieses Beispiel zeigt, wie ausgewählte Seiten aus einem sekundären PDF an einer bestimmten Position des Originaldokuments hinzugefügt werden, um ein kombiniertes PDF mit präziser Seitenplatzierung zu erstellen.
---

Das Einfügen von Seiten in ein bestehendes PDF ist ein häufiges Bedürfnis beim Kombinieren von Dokumenten, Hinzufügen von Inhalten oder Umstrukturieren von Berichten. Mit Aspose.PDF for Python können Entwickler programmgesteuert Seiten aus einem PDF in ein anderes an einem angegebenen Ort einfügen.

Dieser Artikel zeigt, wie die Insert-Methode des [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) Klasse. Indem Sie die einzufügenden Seitenzahlen und den Zielort angeben, können Sie Inhalte aus verschiedenen PDFs zusammenführen, während die ursprüngliche Formatierung und Struktur beibehalten werden.

1. Erstelle ein PdfFileEditor-Objekt.
1. Definieren Sie die Einfügeposition und die Seiten.
1. Seiten einfügen.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Insert Pages into PDF
def insert_pages_into_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page number where new pages will be inserted (1-based index)
    insert_page_number = 2

    pdf_editor.insert(infile, insert_page_number, sample_file, [1, 2], outfile)
```
