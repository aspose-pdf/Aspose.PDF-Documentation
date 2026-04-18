---
title: Extracción básica de texto usando Python
linktitle: Extracción básica de texto
type: docs
weight: 10
url: /es/python-net/basic-text-extraction/
description: Aprenda cómo extraer texto de documentos PDF usando Aspose.PDF for Python — de todas las páginas a la vez o de una página específica.
lastmod: "2025-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraer texto de todas las páginas de un documento PDF

Usar [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) para capturar todo el texto de cada página de un documento PDF y escribirlo en un archivo de texto. Este enfoque es ideal para convertir PDFs a texto buscable, realizar análisis de contenido, o preparar el texto para indexación y procesamiento posterior.

1. Abra el documento PDF usando [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Crear un `TextAbsorber` instancia.
1. Llamar `document.pages.accept(text_absorber)` para escanear todas las páginas.
1. Recuperar el texto extraído de `text_absorber.text`.
1. Escribe el resultado en un archivo de texto de salida.

```python
import os
import aspose.pdf as ap


def extract_text_from_all_pages(infile, outfile):
    """
    Extract all text from every page of the PDF and write to an output text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    # Open the PDF document
    document = ap.Document(infile)
    # Create a TextAbsorber to extract text
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber for all pages
    document.pages.accept(text_absorber)
    # Get extracted text
    extracted_text = text_absorber.text
    # Write the text to an output file
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```

## Extraer texto de una página específica

Aplicar [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) a una sola página para aislar y guardar texto de esa sección de un documento de varias páginas. Esto es útil cuando necesitas contenido de solo una página — por ejemplo, una factura, una sección de informe o un resumen de formulario.

1. Abra el documento PDF usando [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Crear un `TextAbsorber` instancia.
1. Llamar `accept` en la página de destino: `document.pages[page_number].accept(text_absorber)`.
1. Recupera el texto extraído y escríbelo en un archivo.

```python
import os
import aspose.pdf as ap


def extract_text_from_page(infile, outfile, page_number):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1-based page index to extract.
    """
    document = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber on only the specified page
    document.pages[page_number].accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```
