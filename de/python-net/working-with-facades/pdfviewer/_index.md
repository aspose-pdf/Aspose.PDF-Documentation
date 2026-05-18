---
title: PdfViewer-Klasse
type: docs
weight: 135
url: /de/python-net/pdfviewer-class/
description: Erfahren Sie, wie Sie die PdfViewer-Klasse in Aspose.PDF for Python via .NET verwenden, um alle PDF-Seiten zu dekodieren, eine bestimmte Seite zu dekodieren und viewerbezogene PDF-Metadaten zu untersuchen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dekodieren Sie PDF-Seiten und prüfen Sie Viewer-Daten in Python mit PdfViewer.
Abstract: Dieser Artikel erklärt, wie Sie die PdfViewer-Fassade in Aspose.PDF for Python via .NET für Seiten-Dekodierung und viewerbezogene Prüfaufgaben verwenden. Erfahren Sie, wie Sie alle PDF-Seiten dekodieren, eine bestimmte Seite rendern und Eigenschaften wie Seitenanzahl, Koordinatentyp und Auflösung prüfen.
---

Aspose.PDF for Python via .NET stellt die [PdfViewer](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfviewer/) Fassade für die Arbeit mit PDF-Anzeige- und Seiten-Decodierungsszenarien. Ein gängiger Anwendungsfall ist das Konvertieren von PDF-Seiten in Bildobjekte, die dann auf die Festplatte gespeichert werden können.

## Erstellen Sie einen wiederverwendbaren PdfViewer-Helper

Bevor Sie Seiten dekodieren oder Viewer-bezogene Eigenschaften lesen, erstellen Sie einen kleinen Helfer, der initialisiert und zurückgibt. `PdfViewer` Instanz. Dies hält die nachfolgenden Beispiele eigenständig und verdeutlicht, wie das Viewer-Objekt erstellt wird, bevor es an ein PDF-Dokument gebunden wird.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades


def _create_viewer() -> pdf_facades.PdfViewer:
    """Create a PdfViewer configured for decoding examples."""
    viewer = pdf_facades.PdfViewer()
    viewer.coordinate_type = ap.PageCoordinateType.MEDIA_BOX
    viewer.resolution = 150
    viewer.scale_factor = 1.0
    viewer.show_hidden_areas = False
    return viewer
```

## Alle PDF-Seiten dekodieren

Verwenden `decode_all_pages()` wenn Sie jede Seite im PDF in ein separates Bild konvertieren möchten. Die zurückgegebenen Seitenbilder können dann einzeln in ein Ausgabeverzeichnis gespeichert werden.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_all_pages(infile: str, output_dir: str) -> None:
    """Decode all pages of a PDF document into image files."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        decoded_pages = viewer.decode_all_pages()

        for index, page_image in enumerate(decoded_pages, start=1):
            image_path = path.join(output_dir, f"decode_all_pages_{index}.png")
            page_image.save(image_path)
    finally:
        viewer.close_pdf_file()
```

## Dekodiere eine bestimmte PDF-Seite

Verwenden `decode_page()` wenn Sie nur eine Seite aus dem Dokument benötigen. Dies ist nützlich beim Erzeugen von Vorschaubildern, Miniaturansichten oder seitenbezogenen Exporten.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_specific_page(infile: str, outfile: str, page_number: int = 1) -> None:
    """Decode a specific PDF page into an image file."""
    viewer = _create_viewer()
    try:
        viewer.bind_pdf(infile)
        page_image = viewer.decode_page(page_number)
        page_image.save(outfile)

    finally:
        viewer.close()
```

## PDF-Metadaten prüfen

Der `inspect_pdf_metadata` Die Funktion demonstriert, wie ein PDF-Dokument geöffnet und grundlegende, betrachterbezogene Metadaten mit Aspose.PDF abgerufen werden. Sie konzentriert sich darauf, Informationen zu extrahieren, die beschreiben, wie das Dokument interpretiert und angezeigt wird, anstatt dessen Inhalt.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def inspect_pdf_metadata(infile: str) -> None:
    """Open a PDF and print page-count related viewer metadata."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        print(f"Page count: {viewer.page_count}")
        print(f"Coordinate type: {viewer.coordinate_type}")
        print(f"Resolution: {viewer.resolution}")
    finally:
        viewer.close_pdf_file()
```
