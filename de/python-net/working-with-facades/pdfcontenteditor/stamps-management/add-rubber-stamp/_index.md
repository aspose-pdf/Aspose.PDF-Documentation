---
title: Rubber-Stempel hinzufügen
type: docs
weight: 10
url: /de/python-net/add-rubber-stamp/
description: Dieses Beispiel bindet ein Eingabe‑PDF, fügt den ersten vier Seiten einen grünen “Approved”‑Rubber‑Stempel hinzu und speichert das geänderte Dokument.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rubber‑Stempel‑Annotation zu einem PDF mit PdfContentEditor in Python hinzufügen
Abstract: Dieses Beispiel demonstriert, wie man mithilfe von Aspose.PDF for Python via the Facades API eine Rubber‑Stempel‑Annotation zu einem PDF‑Dokument hinzufügt. Rubber‑Stempel ermöglichen es, Seiten visuell mit Genehmigungen, Überprüfungen oder benutzerdefinierten Etiketten zu kennzeichnen.
---

Rubber‑Stempel‑Annotationen werden häufig in PDFs verwendet, um Genehmigungen, Überprüfungsstatus oder andere Notizen anzuzeigen. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Sie können ein Rechteck für den Stempel definieren, dessen Text und Kommentare festlegen, eine Farbe wählen und ihn auf mehrere Seiten eines Dokuments anwenden.

1. Erstellen Sie eine PdfContentEditor-Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Durchlaufen Sie die Seiten 1–4.
1. Fügen Sie eine Gummistempel-Anmerkung mit benutzerdefiniertem Text, Kommentaren und Farbe hinzu.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_rubber_stamp(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    for i in range(1, 5):
        content_editor.create_rubber_stamp(
            i,
            apd.Rectangle(120, 450, 180, 60),
            "Approved",
            "Approved by reviewer",
            apd.Color.green,
        )
    # Save updated document
    content_editor.save(outfile)
```
