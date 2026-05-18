---
title: Stempel nach ID löschen
type: docs
weight: 85
url: /de/python-net/delete-stamp-by-ids-examples/
description:
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gummistempel in einem PDF anhand einzelner oder mehrerer IDs mithilfe von PdfContentEditor löschen
Abstract: Dieses Beispiel zeigt, wie man Gummistempel-Anmerkungen aus einem PDF anhand ihrer eindeutigen IDs mit Aspose.PDF für Python via der Facades-API entfernt. Es behandelt sowohl das Löschen nach einzelner ID als auch nach mehreren IDs.
---

Beim Arbeiten mit PDFs, die mehrere Stempel enthalten, ist es oft erforderlich, bestimmte Stempel zu entfernen, ohne andere zu beeinflussen. Mit ID‑basiertem Löschen können Sie genau steuern, welche Stempel entfernt werden:

- 'delete_stamp_by_id(stamp_id, page_number)' – löscht einen einzelnen Stempel anhand seiner ID auf einer bestimmten Seite
- 'delete_stamp_by_ids(page_number, stamp_ids)' – löscht mehrere Stempel anhand ihrer IDs auf einer angegebenen Seite

1. Erstelle ein [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Fügen Sie zwei Gummistempel mit eindeutigen IDs hinzu.
1. Löschen Sie Stempel mit sowohl Einzel-ID- als auch Mehrfach-ID-Löschmethoden.
1. Speichere das aktualisierte PDF.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_ids_examples(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Create two stamps on page 1 so they can be deleted by ID
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 320, 180, 60),
        "Draft",
        "Delete by single ID",
        apd.Color.orange,
    )
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 250, 180, 60),
        "Draft",
        "Delete by multiple IDs",
        apd.Color.orange,
    )

    # Delete by single ID overload and by IDs overload
    content_editor.delete_stamp_by_id(1, 1)
    content_editor.delete_stamp_by_ids(1, [2])

    # Save updated document
    content_editor.save(outfile)
```

