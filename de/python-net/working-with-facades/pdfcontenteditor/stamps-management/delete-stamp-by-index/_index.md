---
title: Stempel nach Index löschen
type: docs
weight: 50
url: /de/python-net/delete-stamp-by-index/
description: Dieses Beispiel erstellt zwei Gummistempel auf Seite 2. Anschließend kann ein Stempel gelöscht werden, indem sein Index angegeben wird.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Löschen eines Gummistempels nach Index in einem PDF mit PdfContentEditor in Python
Abstract: Dieses Beispiel zeigt, wie man eine Gummistempel-Anmerkung in einem PDF anhand ihres Index mit Aspose.PDF für Python via the Facades API löscht. Es zeigt, wie man mehrere Stempel hinzufügt und dann einen davon basierend auf ihrer Reihenfolge auf der Seite löscht.
---

Wenn mehrere Gummistempel auf einer Seite vorhanden sind, können Sie einen bestimmten mithilfe seines Index löschen. Die Methode delete_stamp() ermöglicht das Entfernen von Anmerkungen gemäß ihrer Reihenfolge, was nützlich ist, wenn Sie keine Stempel-IDs verfolgen, aber deren Reihenfolge kennen.

1. Erstelle ein [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Binden Sie die Eingabe‑PDF‑Datei an die PdfContentEditor‑Instanz mit bind_pdf(infile).
1. Rufen Sie 'delete_stamp(1, [2, 3])' auf, um den Stempel mit Index 1 von den Seiten 2 und 3 zu entfernen.
1. Speichern Sie das modifizierte PDF-Dokument mit save(outfile) in die Ausgabedatei.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    content_editor.delete_stamp(1, [2, 3])
    # Save updated document
    content_editor.save(outfile)
```
