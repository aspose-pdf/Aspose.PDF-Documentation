---
title: Popup-Anmerkungen hinzufügen
type: docs
weight: 40
url: /de/python-net/add-popup-annotation/
description: Dieses Beispiel lädt eine PDF, fügt der ersten Seite eine Popup-Anmerkung hinzu und speichert das modifizierte Dokument. Das Popup ist standardmäßig sichtbar und zeigt den angegebenen Kommentartext an.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Popup-Anmerkungen zu einer PDF mit Python hinzufügen
Abstract: Dieses Beispiel zeigt, wie man mithilfe von Aspose.PDF for Python via the Facades API eine Popup-Anmerkung in ein PDF-Dokument einfügt. Es erklärt, wie man den Popup‑Bereich definiert, den Anmerkungstext festlegt, die Sichtbarkeit steuert und das aktualisierte Dokument speichert.
---

Popup-Anmerkungen sind nützlich, um Kommentare, Erklärungen oder interaktive Notizen in PDF-Dateien hinzuzufügen. Mit [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie Popup-Anmerkungen programmgesteuert erstellen, indem Sie den Ort, den Inhalt, die Sichtbarkeit und die Seitenzahl angeben.

1. Erstellen Sie das PdfContentEditor-Objekt.
1. Binden Sie das Eingabe-PDF.
1. Definieren Sie das Rechteck der Popup-Annotation.
1. Fügen Sie die Popup-Annotation hinzu.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_popup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add popup annotation to page 1
    content_editor.create_popup(
        apd.Rectangle(220, 520, 180, 80),
        "This is a popup annotation",
        True,
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```
