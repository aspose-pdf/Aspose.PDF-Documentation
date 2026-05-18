---
title: Stempel global löschen
type: docs
weight: 60
url: /de/python-net/delete-stamps-globally/
description: Dieses Beispiel demonstriert, wie man Gummistempel-Anmerkungen global über alle Seiten in einer PDF mithilfe von Aspose.PDF for Python via the Facades API löscht. Es zeigt, wie man Stempel anhand ihrer ID entfernt, ohne einzelne Seiten angeben zu müssen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gummistempel global in einer PDF mit PdfContentEditor in Python löschen
Abstract: Dieses Beispiel demonstriert, wie man Gummistempel-Anmerkungen global über alle Seiten in einer PDF mithilfe von Aspose.PDF for Python via the Facades API löscht. Es zeigt, wie man Stempel anhand ihrer ID entfernt, ohne einzelne Seiten angeben zu müssen.
---

Beim Arbeiten mit mehreren Seiten kann es erforderlich sein, bestimmte Stempel im gesamten Dokument zu entfernen. Die Methoden 'delete_stamp_by_id()' und 'delete_stamp_by_ids()' ermöglichen das globale Löschen von Stempeln anhand ihrer Kennungen und beseitigen die Notwendigkeit, jede Seite manuell zu durchlaufen.

1. Erstelle ein [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Fügen Sie Gummistempel zu mehreren Seiten hinzu.
1. Stempel global mithilfe ihrer IDs löschen.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamps_globally(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Add stamps across multiple pages so global deletion is meaningful
    for page in range(1, 5):
        content_editor.create_rubber_stamp(
            page,
            apd.Rectangle(120, 500, 180, 60),
            "Draft",
            "Stamp for global deletion",
            apd.Color.gray,
        )

    # delete_stamp_by_id without page number removes stamp ID from all pages
    content_editor.delete_stamp_by_id(1)
    # delete_stamp_by_ids without page number removes a list of IDs from all pages
    content_editor.delete_stamp_by_ids([2, 3])

    # Save updated document
    content_editor.save(outfile)
```
