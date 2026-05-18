---
title: Anhänge entfernen
type: docs
weight: 50
url: /de/python-net/remove-attachments/
description: Dieses Beispiel bindet ein Eingabe‑PDF, löscht alle Anhänge und speichert das modifizierte PDF ohne eingebettete Dateien.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Alle Anhänge aus einem PDF mit Python entfernen
Abstract: Dieses Beispiel zeigt, wie alle Dateianhänge aus einem PDF‑Dokument mithilfe von Aspose.PDF for Python über die Facades‑API entfernt werden können. Es zeigt, wie ein PDF gebunden, eingebettete Anhänge gelöscht und das aktualisierte Dokument gespeichert werden.
---

PDFs können Anhänge wie Dokumente, Bilder oder andere Dateien enthalten. Es gibt Szenarien, in denen Sie ein PDF aus Sicherheits‑, Datenschutz‑ oder Verteilungsgründen von allen Anhängen bereinigen müssen. Verwenden [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie programmgesteuert alle eingebetteten Anhänge in einem Dokument entfernen.

1. Erstellen Sie das PdfContentEditor-Objekt. 
1. Binden Sie das Eingabe-PDF.
1. Alle Anhänge löschen.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_attachments(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove all attachments from document
    content_editor.delete_attachments()
    # Save updated document
    content_editor.save(outfile)
```
