---
title: Stempel zu PDF hinzufügen
type: docs
weight: 40
url: /de/python-net/add-stamp/
description: Erfahren Sie, wie Sie mit PdfFileStamp in Python einen Stempel zu PDF‑Seiten hinzufügen.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Textstempel zu PDF in Python hinzufügen
Abstract: Dieser Artikel erklärt, wie man Stempelinhalt zu PDF‑Dokumenten mit Aspose.PDF for Python via .NET unter Verwendung der PdfFileStamp‑Fassade hinzufügt. Er zeigt, wie man einen Stempel erstellt, ihn auf der Seite positioniert, Drehung und Transparenz steuert und das aktualisierte PDF speichert.
---

Aspose.PDF for Python via .NET stellt die [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) Fassade zum Hinzufügen wiederholter Inhalte zu PDF‑Seiten. Zusätzlich zu Kopf‑ und Fußzeilen sowie Seitenzahlen können Sie sie verwenden, um textbasierte Stempel auf jeder Seite eines Dokuments zu platzieren.

## Stempel zu einem PDF hinzufügen

Nachdem der Stempel konfiguriert wurde, binden Sie das Eingabe‑PDF an `PdfFileStamp`, füge den Stempel hinzu und speichere die Ausgabedatei. Dies wendet den konfigurierten Stempel im gesamten Dokument an.

```python
import sys
from os import path

import aspose.pdf.facades as pdf_facades

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def add_stamp_to_pdf(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to a PDF file."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
