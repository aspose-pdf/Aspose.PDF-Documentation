---
title: Anwendungslink hinzufügen
type: docs
weight: 10
url: /de/python-net/add-application-link/
description: Dieses Beispiel bindet ein Eingabe‑PDF, fügt einen Anwendungs‑Startlink auf der ersten Seite hinzu und speichert das geänderte Dokument.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Anwendungs‑Startlink zu einem PDF mit PdfContentEditor in Python hinzufügen
Abstract: Dieses Beispiel demonstriert, wie man einen Anwendungs‑Startlink zu einem PDF‑Dokument mithilfe von Aspose.PDF for Python über die Facades‑API hinzufügt. Es zeigt, wie man einen anklickbaren Bereich erstellt, der bei Anklicken eine bestimmte Anwendung öffnet, und das aktualisierte PDF speichert.
---

PDF kann interaktive Elemente wie Links enthalten, die externe Anwendungen starten. Mit [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie einen rechteckigen Bereich auf einer Seite definieren, der beim Anklicken eine bestimmte ausführbare Datei öffnet.

1. Erstellen Sie eine PdfContentEditor-Instanz.
1. Binden Sie das Eingabe-PDF-Dokument.
1. Definieren Sie einen rechteckigen Bereich für den anklickbaren Link.
1. Geben Sie den Anwendungspfad zum Starten an.
1. Legen Sie die Linkfarbe fest.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_application_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add application launch link
    content_editor.create_application_link(
        apd.Rectangle(180, 530, 260, 20),
        "notepad.exe",
        1,
        apd.Color.purple,
    )
    # Save updated document
    content_editor.save(outfile)
```
