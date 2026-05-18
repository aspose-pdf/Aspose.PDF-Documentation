---
title: Stempel nach ID verschieben
type: docs
weight: 80
url: /de/python-net/move-stamp-by-id-example/
description: In diesem Beispiel wird ein Gummistempel zu Seite 1 hinzugefügt und anschließend mithilfe seiner ID an eine neue Position verschoben, bevor das aktualisierte Dokument gespeichert wird.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Verschieben eines Gummistempels per ID in einem PDF mit PdfContentEditor in Python
Abstract: Dieses Beispiel zeigt, wie man eine vorhandene Gummistempel-Anmerkung in einem PDF mit Aspose.PDF for Python über die Facades-API neu positioniert. Es wird gezeigt, wie man einen Stempel erstellt und ihn dann programmgesteuert mithilfe seiner ID verschiebt.
---

Nachdem Sie eine Gummistempel-Anmerkung zu einem PDF hinzugefügt haben, müssen Sie möglicherweise deren Position anpassen. Die 'move_stamp_by_id()'-Methode ermöglicht es, einen Stempel basierend auf seinem Bezeichner zu verschieben, ohne ihn neu zu erstellen. Dies ist nützlich in automatisierten Workflows, bei denen die Platzierung des Stempels dynamisch angepasst werden muss.

1. Erstelle ein [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Eine Gummistempel-Anmerkung hinzufügen.
1. Verschieben Sie den Stempel mithilfe seiner ID.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_id_example(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(300, 420, 180, 60),
        "Approved",
        "Move this stamp by ID",
        apd.Color.green,
    )

    # Move stamp by ID overload
    content_editor.move_stamp_by_id(1, 1, 240, 360)

    # Save updated document
    content_editor.save(outfile)
```    
