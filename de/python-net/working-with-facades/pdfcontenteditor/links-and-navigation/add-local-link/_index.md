---
title: Lokalen Link hinzufügen
type: docs
weight: 40
url: /de/python-net/add-local-link/
description: Dieses Beispiel bindet ein Eingabe‑PDF, fügt auf Seite 1 einen rot‑gefärbten lokalen Link hinzu, der auf Seite 1 verweist, und speichert das geänderte Dokument.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Lokalen Link zu einem PDF mit PdfContentEditor in Python hinzufügen
Abstract: Dieses Beispiel demonstriert, wie man einen lokalen Link zu einem PDF‑Dokument mit Aspose.PDF for Python via the Facades API hinzufügt. Es zeigt, wie man einen anklickbaren Bereich erstellt, der zu einer anderen Seite im selben PDF navigiert, und das aktualisierte Dokument speichert.
---

Lokale Links in PDFs ermöglichen eine schnelle Navigation zwischen Seiten im selben Dokument. Mit [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie ein anklickbares Rechteck definieren, das eine Seite mit einer anderen verknüpft und die Benutzerfreundlichkeit sowie Navigation des Dokuments verbessert.

1. Erstellen Sie eine PdfContentEditor-Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Definieren Sie ein Rechteck für den anklickbaren lokalen Link.
1. Spezifiziere die Quellseite und die Zielseite.
1. Setzen Sie die Linkfarbe.
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


def add_local_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a local link on page 1 to destination page 1
    content_editor.create_local_link(
        apd.Rectangle(120, 620, 220, 20),
        1,
        1,
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
