---
title: PDF-Booklet erstellen
type: docs
weight: 20
url: /de/python-net/create-pdf-booklet/
description: Erstellen Sie ein Booklet‑Stil‑PDF aus einem vorhandenen Dokument mit Aspose.PDF for Python
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Erstellen Sie ein PDF-Booklet aus einem vorhandenen PDF mit Python
Abstract: Lernen Sie, wie Sie ein Booklet‑Stil‑PDF aus einem vorhandenen Dokument mit Aspose.PDF for Python erstellen. Dieses Beispiel zeigt, wie die Klasse PdfFileEditor verwendet wird, um Seiten neu anzuordnen, sodass sie als Booklet gedruckt und gefaltet werden können. Die Methode ordnet die Seiten automatisch, um ein korrektes Booklet‑Layout zu erzeugen.
---

Das Erstellen von Booklet‑Stil‑Dokumenten ist eine häufige Anforderung beim Vorbereiten von PDFs für den Druck. In einem Booklet‑Layout werden die Seiten neu angeordnet, sodass sie nach dem Drucken und Falten in der richtigen Reihenfolge erscheinen.

Mit Aspose.PDF for Python können Entwickler problemlos ein Standard‑PDF in ein Booklet konvertieren, indem sie die [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) Klasse. Die Methode 'make_booklet' reorganisiert automatisch die Seiten des Eingabedokuments und erzeugt ein neues PDF, das für Broschürendruck optimiert ist.

1. Öffnen Sie ein bestehendes PDF-Dokument.
1. Erstellen Sie eine PdfFileEditor‑Instanz.
1. Verwenden Sie die Methode make_booklet, um die Seiten neu zu organisieren.
1. Speichern Sie die Ausgabe als broschürenfertige PDF-Datei.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create PDF Booklet
def create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    booklet_maker.make_booklet(FileIO(infile), FileIO(outfile, "w"))
```

Dieses Codefragment zeigt, wie die Methode 'try_make_booklet' der [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) Klasse verwendet wird, um Seiten für den Druck von Broschüren neu anzuordnen, ohne Ausnahmen zu werfen, falls der Vorgang fehlschlägt.

Ein Broschürenlayout ordnet die Seiten neu, sodass das Dokument nach dem Druck und Falten in der richtigen Reihenfolge gelesen wird. Die Automatisierung dieses Vorgangs sorgt für konsistente Ergebnisse und eliminiert die Notwendigkeit manueller Seitenumordnung.

Die Methode 'try_make_booklet' funktioniert ähnlich wie 'make_booklet', jedoch mit einem wichtigen Unterschied:

- 'make_booklet' wirft eine Ausnahme, wenn die Operation fehlschlägt.
- 'try_make_booklet' gibt True oder False zurück, wodurch Entwickler Fehler sicherer handhaben können.

1. Öffnen Sie ein bestehendes PDF-Dokument.
1. Erstellen Sie eine PdfFileEditor‑Instanz.
1. Versuchen Sie, das Booklet zu erstellen.
1. Verarbeiten Sie das Ergebnis.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def try_create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    # The try_make_booklet method is like the make_booklet method,
    # except the try_make_booklet method does not throw an exception if the operation fails.
    if not booklet_maker.try_make_booklet(FileIO(infile), FileIO(outfile, "w")):
        print("Failed to create booklet.")
```
