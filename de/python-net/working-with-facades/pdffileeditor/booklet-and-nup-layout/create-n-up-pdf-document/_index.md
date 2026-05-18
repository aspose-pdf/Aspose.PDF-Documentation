---
title: N-Up PDF-Dokument erstellen
type: docs
weight: 10
url: /de/python-net/create-n-up-pdf-document/
description: Erfahren Sie, wie Sie ein N-Up PDF-Dokument erstellen, während Sie potenzielle Fehler sicher mit Aspose.PDF for Python behandeln.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: N-Up PDF-Layout in Python erstellen
Abstract: Erfahren Sie, wie Sie ein N-Up PDF-Layout mit Aspose.PDF for Python erzeugen. Dieses Beispiel zeigt, wie mehrere Seiten eines PDF-Dokuments zu einer einzelnen Seite kombiniert werden, indem die Methode ‘make_n_up’ oder ‘try_make_n_up’ der Klasse PdfFileEditor verwendet wird.
---

Ein N-Up-Layout platziert mehrere Seiten eines PDF-Dokuments in einem Rasterformat auf einer einzigen Seite. Dieses Layout wird häufig beim Drucken von Präsentationen, Handouts oder Berichten verwendet, bei denen mehrere Seiten gleichzeitig angezeigt werden können.

Mit Aspose.PDF for Python können Entwickler schnell ein N-Up-Dokument erstellen, indem sie die Anzahl von Zeilen und Spalten angeben, die bestimmen, wie viele Originalseiten auf jeder Ausgabeseite erscheinen.

In diesem Codeausschnitt verwendet die Methode 'make_n_up' der [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) Klasse ordnet die Seiten des Eingabe‑PDFs in einem 2 × 2‑Raster an, sodass vier Originalseiten auf einer Seite im Ausgabedokument erscheinen.

Im gezeigten Beispiel verwendet das Layout 2 Zeilen und 2 Spalten und erzeugt vier Seiten pro Blatt:

1. Öffnen Sie die Quell-PDF-Datei.
1. Erstellen Sie eine PdfFileEditor‑Instanz.
1. Geben Sie die Anzahl der Zeilen und Spalten für das N‑Up‑Layout an.
1. Erzeuge ein neues PDF mit kombinierten Seiten.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    nup_maker.make_n_up(
        FileIO(infile), FileIO(outfile, "w"), 2, 2
    )  # 2 rows and 2 columns for N-Up layout
```

Aspose.PDF for Python via .NET ermöglicht das Erzeugen von N-Up-Layouts mit der PdfFileEditor-Klasse. Die Methode 'try_make_n_up' funktioniert ähnlich wie make_n_up, gibt jedoch anstelle einer Ausnahme bei einem Fehlschlag einen booleschen Wert zurück, der angibt, ob der Vorgang erfolgreich war.

Das N-Up-Layout ordnet mehrere PDF-Seiten auf einer einzelnen Seite an, wobei ein Raster verwendet wird, das durch Zeilen und Spalten definiert ist.

Die Methode 'try_make_n_up' bietet eine sicherere Möglichkeit, diesen Vorgang auszuführen, weil:

- Sie gibt True zurück, wenn das Layout erfolgreich erstellt wurde.
- Gibt False zurück, wenn die Operation fehlschlägt
- Unterbricht die Programmausführung nicht mit Ausnahmen

Im nachfolgenden Beispiel wird das Dokument mit einem 2 × 2‑Raster angeordnet, das vier Originalseiten auf jeder Ausgabeseite platziert.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def try_create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    if not nup_maker.try_make_n_up(FileIO(infile), FileIO(outfile, "w"), 2, 2):
        print("Failed to create N-Up PDF document.")
```
