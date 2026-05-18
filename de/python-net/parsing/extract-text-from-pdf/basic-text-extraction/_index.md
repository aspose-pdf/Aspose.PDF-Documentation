---
title: Grundlegende Textextraktion mit Python
linktitle: Grundlegende Textextraktion
type: docs
weight: 10
url: /de/python-net/basic-text-extraction/
description: Erfahren Sie, wie Sie Text aus PDF-Dokumenten mit Aspose.PDF for Python — entweder von allen Seiten gleichzeitig oder von einer bestimmten Seite.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Text aus allen Seiten eines PDF-Dokuments extrahieren

Verwenden [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) um den gesamten Text jeder Seite eines PDF-Dokuments zu erfassen und in eine Textdatei zu schreiben. Dieser Ansatz eignet sich gut zum Konvertieren von PDFs in durchsuchbaren Text, zur Durchführung von Inhaltsanalysen oder zur Vorbereitung von Text für die Indizierung und nachgelagerte Verarbeitung.

1. Öffnen Sie das PDF-Dokument mit [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Erstelle ein `TextAbsorber` Instanz.
1. Anruf `document.pages.accept(text_absorber)` Alle Seiten scannen.
1. Rufen Sie den extrahierten Text aus `text_absorber.text`.
1. Schreiben Sie das Ergebnis in eine Ausgabedatei.

```python
import os
import aspose.pdf as ap


def extract_text_from_all_pages(infile, outfile):
    """
    Extract all text from every page of the PDF and write to an output text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    # Open the PDF document
    document = ap.Document(infile)
    # Create a TextAbsorber to extract text
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber for all pages
    document.pages.accept(text_absorber)
    # Get extracted text
    extracted_text = text_absorber.text
    # Write the text to an output file
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```

## Text aus einer bestimmten Seite extrahieren

Anwenden [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) auf eine einzelne Seite, um Text aus diesem Abschnitt eines mehrseitigen Dokuments zu isolieren und zu speichern. Das ist nützlich, wenn Sie Inhalte nur von einer Seite benötigen — zum Beispiel eine Rechnung, einen Berichtabschnitt oder eine Formularzusammenfassung.

1. Öffnen Sie das PDF-Dokument mit [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Erstelle ein `TextAbsorber` Instanz.
1. Anruf `accept` auf der Zielseite: `document.pages[page_number].accept(text_absorber)`.
1. Rufen Sie den extrahierten Text ab und schreiben Sie ihn in eine Datei.

```python
import os
import aspose.pdf as ap


def extract_text_from_page(infile, outfile, page_number):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1-based page index to extract.
    """
    document = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber on only the specified page
    document.pages[page_number].accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```
