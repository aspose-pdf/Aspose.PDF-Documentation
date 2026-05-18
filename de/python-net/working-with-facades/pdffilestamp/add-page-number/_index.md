---
title: Seitenzahl zum PDF hinzufügen
type: docs
weight: 30
url: /de/python-net/page-number/
description: Erfahren Sie, wie Sie Seitenzahlen zu PDF-Dokumenten mit PdfFileStamp in Python hinzufügen.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Seitenzahlen zu PDF in Python hinzufügen
Abstract: Dieser Artikel erklärt, wie man Seitenzahlen zu PDF-Dokumenten mit Aspose.PDF for Python via .NET unter Verwendung der PdfFileStamp-Fassade hinzufügt. Er zeigt, wie man Seitenzahlen mit der Standardplatzierung hinzufügt, sie an benutzerdefinierten Koordinaten positioniert und Ausrichtung sowie Ränder steuert.
---

Aspose.PDF for Python via .NET stellt die [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) Fassade zum Hinzufügen wiederholter Inhalte zu PDF-Seiten. Sie können sie verwenden, um Seitenzahlen mit Standardplatzierung einzufügen, sie an bestimmten Koordinaten zu positionieren oder ihre Ausrichtung und Ränder zu steuern.

## Fügen Sie Seitenzahlen mit der Standardplatzierung hinzu

Verwenden `add_page_number()` ohne zusätzliche Positionsargumente, wenn Sie Seitenzahlen an der Standardposition hinzufügen möchten. Dies ist der einfachste Weg, jede Seite im Dokument zu nummerieren.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_default(infile: str, outfile: str) -> None:
    """Add centered page numbers to the bottom of each page."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number("Page #")
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Seitenzahlen an benutzerdefinierten Koordinaten hinzufügen

Verwenden Sie die koordinatenbasierte Überladung, wenn Sie Seitenzahlen an einer bestimmten X- und Y-Position auf jeder Seite anzeigen möchten. Dieser Ansatz ist nützlich, wenn das Dokumentlayout eine benutzerdefinierte Platzierung erfordert.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_at_coordinates(infile: str, outfile: str) -> None:
    """Add page numbers at explicit X/Y coordinates."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number("Page #", 300, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Fügen Sie Seitenzahlen mit Ausrichtung und Rändern hinzu

Verwenden Sie die Überladung mit Positions- und Randargumenten, wenn Sie mehr Kontrolle darüber benötigen, wo Seitenzahlen erscheinen. In diesem Beispiel sind die Zahlen an den oberen rechten Bereich der Seite mit expliziten Rändern ausgerichtet.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_with_position_and_margins(infile: str, outfile: str) -> None:
    """Add page numbers using a predefined position and page margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number(
            "Page #",
            pdf_facades.PdfFileStamp.POS_BOTTOM_RIGHT,
            10,
            10,
            10,
            10,
        )
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Seitenzahlen im römischen Stil hinzufügen

Die Funktion 'add_page_numbers_with_roman_style' zeigt, wie man ein PDF-Dokument verbessert, indem man Seitenzahlen mit Großbuchstaben‑römischen Ziffern hinzufügt. Sie nutzt die Klasse PdfFileStamp aus Aspose.PDF, um eine einheitliche Nummerierung über alle Seiten anzuwenden.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_with_roman_style(infile: str, outfile: str) -> None:
    """Add page numbers with a custom start value and Roman numbering."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE
        pdf_stamper.starting_number = 42
        pdf_stamper.add_page_number("Page #", pdf_facades.PdfFileStamp.POS_UPPER_RIGHT)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
