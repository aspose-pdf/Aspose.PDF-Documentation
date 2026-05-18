---
title: Header zum PDF hinzufügen
type: docs
weight: 20
url: /de/python-net/add-header/
description: Erfahren Sie, wie Sie Text‑ und Bild‑Kopfzeilen zu PDF‑Seiten mithilfe von PdfFileStamp in Python hinzufügen.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Text‑ und Bild‑Kopfzeilen zu PDF in Python hinzufügen
Abstract: Dieser Artikel erklärt, wie Sie Kopfzeileninhalt zu PDF‑Dokumenten mit Aspose.PDF for Python via .NET mithilfe der PdfFileStamp‑Fassade hinzufügen. Er zeigt, wie Sie eine Text‑Kopfzeile hinzufügen, eine Bild‑Kopfzeile platzieren und benutzerdefinierte Kopfzeilenränder anwenden, bevor Sie das aktualisierte PDF speichern.
---

Aspose.PDF for Python via .NET stellt die [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) Fassade zum Hinzufügen wiederholter Inhalte zu PDF‑Seiten. Sie können sie verwenden, um Kopfzeilentext oder -bilder oben auf jeder Seite zu platzieren und die Kopfzeilenränder anzupassen, um die Platzierung zu steuern.

## Fügen Sie eine Textüberschrift hinzu

Verwenden `add_header()` mit einem `FormattedText` Objekt, wenn Sie denselben Header-Text auf jeder Seite des PDFs platzieren möchten. Das zweite Argument definiert den oberen Rand für den Header.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_text_header(infile: str, outfile: str) -> None:
    """Add a text header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Header")
        pdf_stamper.add_header(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Bildkopfzeile hinzufügen

Verwenden `add_header()` mit einer Bilddatei oder einem Bild-Stream, wenn die Kopfzeile ein Logo oder eine andere Grafik anzeigen soll. Dies ist nützlich für markenbezogene Dokumentlayouts.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_image_header(infile: str, image_file: str, outfile: str) -> None:
    """Add an image header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_header(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Füge einen Header mit benutzerdefinierten Rändern hinzu

Verwenden Sie die Überladung mit drei Randwerten, wenn Sie mehr Kontrolle über die Platzierung der Kopfzeile benötigen. In diesem Beispiel wird die Kopfzeile mit benutzerdefinierten oberen, linken und rechten Rändern hinzugefügt.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_header_with_margins(infile: str, outfile: str) -> None:
    """Add a text header with top, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText(
            text="Sample Header",
            text_color=ap_pydrawing.Color.blue,
            font_name="Arial",
            text_encoding=pdf_facades.EncodingType.WINANSI,
            embedded=True,
            font_size=12.0,
        )
        pdf_stamper.add_header(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
