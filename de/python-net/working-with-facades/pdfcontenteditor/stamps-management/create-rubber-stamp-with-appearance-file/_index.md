---
title: Gummistempel mit Erscheinungsdatei erstellen
type: docs
weight: 20
url: /de/python-net/create-rubber-stamp-with-appearance-file/
description: Das Beispiel bindet ein Eingabe-PDF, erstellt auf Seite 1 einen Gummistempel, wobei eine Bilddatei als Stempel‑Erscheinung verwendet wird, und speichert das aktualisierte PDF.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gummistempel mit benutzerdefinierter Erscheinung in einem PDF mit PdfContentEditor erstellen
Abstract: Dieses Beispiel zeigt, wie man einer PDF‑Dokument ein Gummistempel‑Annotation mit einer benutzerdefinierten Erscheinung (Bild) hinzufügt, wobei Aspose.PDF for Python via the Facades API verwendet wird. Benutzerdefinierte Stempel ermöglichen das Einbinden von Logos, Unterschriften oder markenbezogenen Grafiken als Teil des Stempels.
---

Gummistempel‑Annotationen können nicht nur mit Text, sondern auch durch Verwendung einer Bilddatei als Erscheinung angepasst werden. Dieser Ansatz ist nützlich, um Unternehmenslogos, Unterschriftsstempel oder andere visuelle Hinweise zu Ihren PDF‑Seiten hinzuzufügen.

1. Erstelle ein [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Definieren Sie ein Rechteck für den Stempel.
1. Verwenden Sie eine benutzerdefinierte Bilddatei, um das Erscheinungsbild des Gummistempels zu definieren.
1. Legen Sie den Text und die Farbe des Stempels fest.
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
