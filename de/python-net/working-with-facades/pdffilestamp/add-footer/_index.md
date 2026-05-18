---
title: Fußzeile zum PDF hinzufügen
type: docs
weight: 10
url: /de/python-net/add-footer/
description: Erfahren Sie, wie Sie Text- und Bildfußzeilen zu PDF‑Seiten mit PdfFileStamp in Python hinzufügen.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Text‑ und Bildfußzeilen zu PDF in Python hinzufügen
Abstract: Dieser Artikel erklärt, wie Sie Fußzeileninhalte zu PDF‑Dokumenten mit Aspose.PDF for Python via .NET unter Verwendung der PdfFileStamp‑Fassade hinzufügen. Er zeigt, wie man eine Textfußzeile hinzufügt, eine Bildfußzeile platziert und benutzerdefinierte Fußzeilenabstände anwendet, bevor das aktualisierte PDF gespeichert wird.
---

Aspose.PDF for Python via .NET stellt die [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) Fassade für das Hinzufügen wiederholter Inhalte zu PDF‑Seiten. Sie können sie verwenden, um Fußzeilentext oder Bilder am unteren Rand jeder Seite zu platzieren und die Fußzeilenränder anzupassen, um die Platzierung zu steuern.

## Füge eine Textfußzeile hinzu

Verwenden `add_footer()` mit einem `FormattedText` Objekt, wenn Sie dieselbe Textfußzeile auf jeder Seite des PDF platzieren möchten. Das zweite Argument legt den unteren Rand fest, der für die Platzierung der Fußzeile verwendet wird.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_text_footer(infile: str, outfile: str) -> None:
    """Add a text footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Footer")
        pdf_stamper.add_footer(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Bildfußzeile hinzufügen

Verwenden `add_footer()` mit einem Bildstrom, wenn die Fußzeile statt Text ein Logo oder ein anderes Bild anzeigen soll. Das Beispiel öffnet die Bilddatei als Binärstrom und platziert sie am unteren Rand jeder Seite.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_image_footer(infile: str, image_file: str, outfile: str) -> None:
    """Add an image footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_footer(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Fügen Sie eine Fußzeile mit benutzerdefinierten Rändern hinzu

Verwenden Sie die Überladung mit drei Randwerten, wenn Sie mehr Kontrolle über die Platzierung der Fußzeile benötigen. In diesem Beispiel wird die Fußzeile mit benutzerdefinierten unteren, linken und rechten Rändern hinzugefügt.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_footer_with_margins(infile: str, outfile: str) -> None:
    """Add a text footer with bottom, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("This footer has margins on all sides.")
        pdf_stamper.add_footer(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
