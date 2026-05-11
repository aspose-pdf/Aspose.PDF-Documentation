---
title: Clase PdfViewer
linktitle: Clase PdfViewer
type: docs
weight: 135
url: /es/python-net/pdfviewer-class/
description: Aprenda cómo usar la clase PdfViewer en Aspose.PDF for Python via .NET para decodificar todas las páginas PDF, decodificar una página específica y examinar los metadatos PDF relacionados con el visor.
lastmod: "2026-05-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Decodifique páginas PDF y examine los datos del visor en Python con PdfViewer
Abstract: Este artículo explica cómo usar la fachada PdfViewer en Aspose.PDF for Python via .NET para tareas de decodificación de páginas e inspección relacionadas con el visor. Aprenda cómo decodificar todas las páginas PDF, renderizar una página específica y examinar propiedades como el número de páginas, el tipo de coordenadas y la resolución.
---

Aspose.PDF for Python via .NET proporciona el [PdfViewer](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfviewer/) fachada para trabajar con la visualización de PDF y escenarios de decodificación de páginas. Un caso de uso común es convertir páginas PDF en objetos de imagen que luego pueden guardarse en el disco.

## Crea un asistente PdfViewer reutilizable

Antes de decodificar páginas o leer propiedades relacionadas con el visor, cree un pequeño asistente que inicialice y devuelva un `PdfViewer` instancia. Esto mantiene los ejemplos a continuación autocontenidos y deja claro cómo se crea el objeto viewer antes de que se vincule a un documento PDF.

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

## Decodificar todas las páginas PDF

Usar `decode_all_pages()` cuando deseas convertir cada página del PDF en una imagen separada. Las imágenes de página devueltas pueden guardarse una por una en un directorio de salida.

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

## Decodificar una página PDF específica

Usar `decode_page()` cuando solo necesitas una página del documento. Esto es útil al generar vistas previas, miniaturas o exportaciones específicas de página.

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

## Inspeccionar metadatos PDF

El `inspect_pdf_metadata` La función demuestra cómo abrir un documento PDF y recuperar metadatos básicos relacionados con el visor usando Aspose.PDF. Se centra en extraer información que describe cómo se interpreta y muestra el documento, en lugar de su contenido.

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
