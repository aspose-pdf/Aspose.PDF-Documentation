---
title: PDF-Dateien in Python erstellen
linktitle: PDF-Dokument erstellen
type: docs
weight: 10
url: /de/python-net/create-pdf-document/
description: Erfahren Sie, wie Sie PDF-Dateien erstellen und durchsuchbare PDFs in Python mit Aspose.PDF for Python via .NET erzeugen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Datei mit Python erstellen
Abstract: Aspose.PDF for Python via .NET ist eine vielseitige API, die für Entwickler entwickelt wurde, um PDF-Dateien innerhalb von Python-Anwendungen, die das .NET-Framework anvisieren, zu manipulieren. Sie ermöglicht es Benutzern, PDF-Dokumente mühelos zu erstellen, zu laden, zu ändern und zu konvertieren. Dieser Artikel bietet eine Schritt-für-Schritt-Anleitung zum Erstellen einer einfachen PDF-Datei mit Aspose.PDF. Der Prozess beinhaltet die Initialisierung eines `Document`-Objekts, das Hinzufügen einer `Page` zum Dokument, das Einfügen eines `TextFragment` in die Absätze der Seite und das Speichern der Datei als PDF. Das beigefügte Python-Code-Snippet demonstriert diese Schritte, indem es ein PDF-Dokument erstellt, das den Text "Hello World!" enthält. Diese API vereinfacht die PDF-Verarbeitung mit minimalem Code und steigert die Produktivität von Entwicklern, die mit PDFs in .NET-Umgebungen arbeiten.
---

**Aspose.PDF for Python via .NET** ist eine PDF-Manipulations-API, die Entwicklern ermöglicht, PDF-Dateien direkt aus Python für .NET-Anwendungen mit nur wenigen Codezeilen zu erstellen, zu laden, zu ändern und zu konvertieren.

Verwenden Sie diese Beispiele, wenn Sie neue PDF-Dateien von Grund auf neu erzeugen oder OCR-Ausgaben in durchsuchbare PDF-Dokumente in Python umwandeln müssen.

## Wie man eine einfache PDF-Datei erstellt

Um ein PDF mit Python via .NET und Aspose.PDF zu erstellen, können Sie die folgenden Schritte befolgen:

1. Erzeugen Sie ein Objekt von [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Klasse
1. Hinzufügen [Seite](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) Objekt zu dem [Seiten](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) Sammlung des Document-Objekts
1. Hinzufügen [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) zu [Absätze](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) Sammlung der Seite
1. Speichern Sie das resultierende PDF Document

```python
import sys
from os import path
import aspose.pdf as ap

def create_new_document(output_pdf):
    """Create a simple PDF with a single “Hello World!” page."""
    document = ap.Document()
    page = document.pages.add()
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    document.save(output_pdf)
```

## Wie man ein durchsuchbares PDF-Dokument erstellt

Aspose.PDF for Python via .NET ermöglicht das Erstellen und Manipulieren vorhandener PDF-Dokumente. Beim Hinzufügen von Text-Elementen zu einer PDF-Datei ist das resultierende PDF durchsuchbar. Wenn jedoch ein Bild, das Text enthält, in eine PDF-Datei konvertiert wird, ist der Inhalt des resultierenden PDFs nicht durchsuchbar. Als Workaround können wir OCR auf die resultierende Datei anwenden, damit sie durchsuchbar wird.

Der folgende Code ist der vollständige Code, um diese Anforderung zu erfüllen:

1. Laden Sie das PDF mit 'ap.Document'.
1. Renderauflösung konfigurieren.
1. Verwenden Sie 'PngDevice.process', um die ausgewählte PDF-Seite in ein Bild zu konvertieren.
1. Führen Sie OCR auf dem erzeugten Bild aus.
1. Erstelle ein neues PDF aus OCR‑Ausgabe.
1. Speichere das durchsuchbare PDF.

```python
import aspose.pdf as ap
import io

# Requires: pip install pytesseract
# Also ensure the Tesseract OCR engine is installed and available on your system PATH.
import pytesseract
from pathlib import Path


# Path to the source PDF
input_pdf_path = "input.pdf"
# Path for the temporary image
temp_image_path = "temp_image.png"
# Path for the searchable PDF
output_pdf_path = "output_searchable.pdf"
page_number = 1
image_stream = io.FileIO(temp_image_path, "w")
try:
    document = ap.Document(input_pdf_path)
    resolution = ap.devices.Resolution(300)
    png_device = ap.devices.PngDevice(resolution)
    png_device.process(document.pages[page_number], image_stream)
    image_stream.close()
    pdf = pytesseract.image_to_pdf_or_hocr(temp_image_path, extension="pdf")
    document = ap.Document(io.BytesIO(pdf))
    document.save(output_pdf_path)
finally:
    image_file = Path(temp_image_path)
    image_file.unlink(missing_ok=True)
```

## Verwandte Dokumentthemen

- [Arbeiten mit PDF-Dokumenten in Python](/pdf/de/python-net/working-with-documents/)
- [PDF-Dokumente in Python formatieren](/pdf/de/python-net/formatting-pdf-document/)
- [PDF‑Dokumente in Python manipulieren](/pdf/de/python-net/manipulate-pdf-document/)
- [PDF‑Dateien in Python optimieren](/pdf/de/python-net/optimize-pdf/)

