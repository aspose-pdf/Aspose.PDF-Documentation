---
title: Stamp-Klasse
type: docs
weight: 150
url: /de/python-net/stamp-class/
description: Erfahren Sie, wie Sie mit der Stamp class arbeiten, um Bild-, PDF- und textbasierte Stempel zu PDF-Dokumenten in Python hinzuzufügen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Python via .NET stellt die [Stempel](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/stamp/) Klasse zum Platzieren wiederverwendbarer visueller Inhalte auf PDF-Seiten. Ein Stempel kann auf Text, einem Bild oder sogar einer Seite aus einem anderen PDF basieren und kann positioniert, rotiert, gestylt und auf bestimmte Seiten beschränkt werden.

Dieser Artikel demonstriert mehrere gängige Stempel-Workflows:

1. Erstellen Sie wiederverwendbare Textressourcen für textbasierte Stempel.
1. Bild- und PDF-Seitenstempel hinzufügen.
1. Stilisierte Textstempel hinzufügen.
1. Beschränken Sie einen Stempel auf ausgewählte Seiten.
1. Einen Hintergrund‑Bildstempel konfigurieren.

Das Beispiel verwendet zwei Hilfsfunktionen: eine erstellt formatierten Text für textbasierte Stempel, und die andere erstellt ein `TextState` Objekt, das zum Gestalten von Textstempeln verwendet wird.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def _create_text_logo(text: str) -> pdf_facades.FormattedText:
    """Create formatted text for text stamp examples."""
    return pdf_facades.FormattedText(
        text,
        drawing.Color.blue,
        drawing.Color.light_gray,
        pdf_facades.FontStyle.HELVETICA_BOLD,
        pdf_facades.EncodingType.WINANSI,
        True,
        14,
    )


def _create_text_state() -> ap.text.TextState:
    """Create a text state used to style text stamps."""
    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.dark_blue
    text_state.font_size = 16
    text_state.font_style = ap.text.FontStyles.BOLD
    return text_state
```

## Bildstempel hinzufügen

Verwenden `bind_image()` wenn der Stempel ein Bild wie ein Logo, Abzeichen oder Symbol anzeigen soll. Nachdem das Bild gebunden wurde, können Sie die Stempel-ID und den Ursprung festlegen, bevor Sie ihn dem Dokument hinzufügen.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to the PDF."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.stamp_id = 1
        stamp.set_origin(36, 520)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Fügen Sie eine PDF‑Seite als Stempel hinzu

Verwenden `bind_pdf()` wenn Sie eine Seite aus einer anderen PDF-Datei als Stempelinhalt verwenden möchten. Dies ist nützlich für Overlays wie Genehmigungen, Vorlagen oder vorgefertigte visuelle Elemente, die in einem separaten Dokument gespeichert sind.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_pdf_page_as_stamp(infile: str, stamp_pdf: str, outfile: str) -> None:
    """Add the first page of another PDF as a stamp."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_pdf(stamp_pdf, 1)
        stamp.page_number = 1
        stamp.set_origin(36, 250)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Fügen Sie einen Textstempel mit Textzustand hinzu

Verwenden `bind_logo()` zusammen mit `bind_text_state()` wenn Sie einen textbasierten Stempel mit benutzerdefiniertem Schriftstil erstellen möchten. Dieser Ansatz ist nützlich für Genehmigungsmarken, Beschriftungen und arbeitsablaufspezifische Anmerkungen.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_text_stamp_with_text_state(infile: str, outfile: str) -> None:
    """Add a text stamp and style it with a TextState object."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_logo(_create_text_logo("Approved by signing workflow"))
        stamp.bind_text_state(_create_text_state())
        stamp.set_origin(36, 700)
        stamp.rotation = 15.0

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Einen Stempel zu bestimmten Seiten hinzufügen

Wenn der Stempel nicht auf jeder Seite erscheinen soll, weisen Sie die Zielseitennummern zu `pages` Eigenschaft. Dieses Beispiel fügt nur auf der ersten Seite einen Bildstempel hinzu.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_stamp_to_specific_pages(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp only to the selected pages."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.pages = [1]
        stamp.set_origin(400, 40)
        stamp.set_image_size(120, 60)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Hintergrundbild-Stempel hinzufügen

Verwenden Sie einen Hintergrundstempel, wenn das Bild hinter dem Seiteninhalt erscheinen soll. Sie können auch die Deckkraft, Drehung, Qualität, Größe und Position des Stempels steuern, um wasserzeichenähnliche Effekte zu erzeugen.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_background_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add a rotated background image stamp with opacity and quality settings."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.is_background = True
        stamp.opacity = 0.35
        stamp.quality = 90
        stamp.rotation = 45.0
        stamp.set_image_size(160, 80)
        stamp.set_origin(200, 300)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Verwandte Facades-Themen

- [Arbeiten mit PDF-Fassaden in Python](/pdf/de/python-net/working-with-facades/)
- [Fügen Sie Kopfzeilen, Fußzeilen und Stempel mit PdfFileStamp hinzu](/pdf/de/python-net/pdffilestamp-class/)
- [Fügen Sie PDF-Dateien in Python einen Seitenstempel hinzu](/pdf/de/python-net/add-stamp/)
