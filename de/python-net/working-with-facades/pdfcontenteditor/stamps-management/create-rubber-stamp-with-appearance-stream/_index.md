---
title: Gummistempel mit Appearance Stream erstellen
type: docs
weight: 30
url: /de/python-net/create-rubber-stamp-with-appearance-stream/
description: Dieses Beispiel lädt ein PDF, erstellt auf Seite 1 einen Gummistempel unter Verwendung einer Bilddatei für das Erscheinungsbild und speichert das geänderte Dokument. ✨
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Erstellen Sie einen Gummistempel mit benutzerdefiniertem Bild‑Erscheinungsbild unter Verwendung von PdfContentEditor in Python
Abstract: Dieses Beispiel zeigt, wie man in einem PDF mithilfe von Aspose.PDF für Python über die Facades‑API eine Gummistempel‑Annotation mit einem benutzerdefinierten Bild‑Erscheinungsbild erstellt. Dieser Ansatz ermöglicht das Anwenden von markenbezogenen oder visuell ansprechenden Stempeln wie Logos, Siegeln oder Unterschriften.
---

Gummistempel‑Annotations können mit einer externen Bilddatei angepasst werden. Anstatt sich nur auf textbasierte Stempel zu verlassen, können Sie ein visuelles Erscheinungsbild definieren (z. B. ein Firmenlogo oder ein Genehmigungsabzeichen) und es auf einer Seite platzieren.

1. Erstelle ein [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Definieren Sie ein Rechteck für die Position des Stempels.
1. Verwenden Sie eine Bilddatei als Stempel-Darstellung.
1. Wenden Sie Text- und Farbeinstellungen an.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_rubber_stamp_with_appearance_file(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create rubber stamp using appearance_file overload (image path)
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(100, 400, 200, 60),
        "Stamp with custom appearance",
        apd.Color.dark_green,
        image_file,
    )
    # Save updated document
    content_editor.save(outfile)
```    
