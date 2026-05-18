---
title: Anhang hinzufügen
type: docs
weight: 10
url: /de/python-net/add-attachment/
description: Dieses Beispiel bindet ein Eingabe-PDF, fügt einer ersten Seite eine externe Datei hinzu und speichert das modifizierte PDF mit dem eingebetteten Anhang.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dateianhänge zu einem PDF mit Python hinzufügen
Abstract: Dieses Beispiel zeigt, wie man externe Dateien an ein PDF-Dokument anhängt, indem man Aspose.PDF for Python via the Facades API verwendet. Es zeigt, wie man ein PDF bindet, Anhänge mit Beschreibungen hinzufügt und das aktualisierte Dokument speichert.
---

Dateianhänge in PDFs ermöglichen es Ihnen, ergänzende Dokumente, Bilder oder andere Ressourcen direkt im PDF zu integrieren. Mit [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie programmgesteuert Dateien an bestimmten Seiten anhängen, den Anhangsnamen festlegen und eine Beschreibung bereitstellen.

1. Erstellen Sie das PdfContentEditor-Objekt.
1. Binden Sie das Eingabe-PDF.
1. Öffnen Sie die Anhangdatei.
1. Fügen Sie den Anhang zum PDF hinzu.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment to page 1
    with open(attachment_file, "rb") as attachment_stream:
        content_editor.add_document_attachment(
            attachment_stream,
            path.basename(attachment_file),
            "This is a sample attachment for demonstration purposes.",
        )
    # Save updated document
    content_editor.save(outfile)
```
