---
title: Stempel nach Index verschieben
type: docs
weight: 90
url: /de/python-net/move-stamp-by-index/
description: Wie man Gummistempel-Anmerkungen in einem PDF anhand ihres Indexes auf einer Seite mit Aspose.PDF für Python neu positioniert
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gummistempel in einem PDF mit indexbasierter Positionierung verschieben
Abstract: Dieses Beispiel zeigt, wie man Gummistempel-Anmerkungen in einem PDF anhand ihres Indexes auf einer Seite mit Aspose.PDF für Python über die Facades API neu positioniert. Es hebt das Erstellen mehrerer Stempel und deren Vorbereitung für Verschiebevorgänge hervor.
---

Beim Bearbeiten von PDFs kann es notwendig sein, die Position vorhandener Gummistempel anzupassen. Dieses Code-Snippet zeigt, wie man das:

- Mehrere Stempel auf derselben Seite hinzufügen
- Bereiten Sie sie für die Neupositionierung mithilfe ihres Index vor.
- Optional können Sie einen Stempel verschieben, indem Sie seine Seite, seinen Index und die neuen Koordinaten angeben.

Die Methode 'move_stamp(page_number, stamp_index, new_x, new_y)' kann Stempel präzise neu positionieren.

1. Erstelle ein [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Objekt.
1. Binden Sie das PDF an den Editor.
1. Fügen Sie einer Seite mehrere Gummistempel hinzu.
1. Speichern Sie das Dokument, bevor Sie Verschiebevorgänge durchführen.
1. Verschieben Sie einen bestimmten Stempel anhand seines Index.
1. Speichere das aktualisierte PDF.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 380, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 480, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )
    content_editor.save(outfile)

    # Move first stamp on page 1 by index
    # content_editor.move_stamp(1, 1, 10, 10)
    # Save updated document
    content_editor.save(outfile)
```    
