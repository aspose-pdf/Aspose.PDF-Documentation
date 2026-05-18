---
title: Weblink hinzufügen
type: docs
weight: 60
url: /de/python-net/add-web-link/
description: Dieses Beispiel bindet eine Eingabe‑PDF, fügt auf Seite 1 eine blaue Weblink‑Annotation ein, die auf die Python‑PDF‑Produktseite von Aspose’s verweist, und speichert das geänderte Dokument.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Weblink zu einer PDF mit PdfContentEditor in Python hinzufügen
Abstract: Dieses Beispiel zeigt, wie man einen Weblink zu einem PDF‑Dokument hinzufügt, indem man Aspose.PDF für Python über die Facades‑API verwendet. Es demonstriert, wie man einen anklickbaren Bereich auf einer Seite erstellt, der eine angegebene URL in einem Webbrowser öffnet, und das aktualisierte Dokument speichert.
---

Weblinks in PDFs ermöglichen es Benutzern, direkt zu Online‑Ressourcen, Websites oder Dokumentationen zu navigieren. Mit [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie einen rechteckigen Bereich auf einer PDF‑Seite definieren, der beim Anklicken eine URL im Standard‑Webbrowser öffnet.

1. Erstellen Sie eine PdfContentEditor-Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Definieren Sie ein Rechteck für den anklickbaren Weblink.
1. Geben Sie die URL, die Seitennummer und die Linkfarbe an.
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


def add_web_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a web link annotation to page 1
    content_editor.create_web_link(
        apd.Rectangle(100, 650, 200, 20),
        "https://products.aspose.com/pdf/python-net/",
        1,
        apd.Color.blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
