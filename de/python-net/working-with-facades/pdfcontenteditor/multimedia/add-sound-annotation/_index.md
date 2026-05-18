---
title: Sound-Annotation hinzufügen
type: docs
weight: 20
url: /de/python-net/add-sound-annotation/
description: Dieses Beispiel bindet ein Eingabe-PDF, fügt auf Seite 1 eine Sound-Annotation hinzu und speichert das modifizierte PDF.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fügen Sie einer PDF mithilfe von PdfContentEditor in Python eine Sound-Annotation hinzu
Abstract: Dieses Beispiel zeigt, wie Audio in ein PDF‑Dokument mit Aspose.PDF for Python via the Facades API eingebettet wird. Es zeigt, wie eine anklickbare Sound-Annotation hinzugefügt wird, die eine Audiodatei direkt im PDF abspielt.
---

Sound-Annotationen in PDFs ermöglichen es Ihnen, Audio‑Inhalte wie Sprachnotizen, Musik oder Soundeffekte zu Ihren Dokumenten hinzuzufügen. Mit [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie ein kleines anklickbares Rechteck auf einer Seite definieren, das bei Aktivierung eine angegebene Audiodatei abspielt.

1. Erstellen Sie eine PdfContentEditor-Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Definieren Sie ein Rechteck für die Sound-Annotation.
1. Geben Sie die Audiodatei, den Namen der Annotation, die Seitenzahl und die Abtastrate an.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_sound_annotation(infile, sound_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add sound annotation to page 1
    content_editor.create_sound(
        apd.Rectangle(80, 450, 30, 30), sound_file, "Speaker", 1, "8000"
    )
    # Save updated document
    content_editor.save(outfile)
```
