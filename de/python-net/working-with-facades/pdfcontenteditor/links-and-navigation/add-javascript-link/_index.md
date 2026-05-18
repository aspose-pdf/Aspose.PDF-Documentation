---
title: JavaScript-Link hinzufügen
type: docs
weight: 30
url: /de/python-net/add-javascript-link/
description: Dieses Beispiel bindet ein Eingabe‑PDF, fügt einen JavaScript‑Link hinzu, der bei einem Klick einen Alarm auslöst, und speichert das modifizierte Dokument.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaScript-Link zu einem PDF mit PdfContentEditor in Python hinzufügen
Abstract: Dieses Beispiel demonstriert, wie man mit Aspose.PDF for Python via the Facades API einen JavaScript‑Link zu einem PDF‑Dokument hinzufügt. Es zeigt, wie man einen anklickbaren Bereich erstellt, der bei einem Klick JavaScript‑Code ausführt, und das aktualisierte PDF speichert.
---

JavaScript-Links in PDFs ermöglichen interaktive Funktionalität wie das Anzeigen von Warnmeldungen, das Durchführen von Berechnungen oder das dynamische Ändern von Dokumenteninhalten. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Sie können ein anklickbares Rechteck auf einer Seite definieren und es mit benutzerdefiniertem JavaScript-Code verknüpfen.

1. Erstellen Sie eine PdfContentEditor-Instanz.
1. Binden Sie das Eingabe-PDF-Dokument.
1. Definieren Sie ein Rechteck für den anklickbaren JavaScript-Link.
1. Geben Sie die Seitenzahl und die Linkfarbe an.
1. Weisen Sie JavaScript-Code zu, der beim Klicken ausgeführt wird.
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


def add_javascript_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript link action
    content_editor.create_java_script_link(
        "app.alert('PdfContentEditor JavaScript link');",
        apd.Rectangle(160, 560, 260, 20),
        1,
        apd.Color.orange,
    )
    # Save updated document
    content_editor.save(outfile)
```
