---
title: Extracción de texto básica usando Python
linktitle: Extracción de texto básica
type: docs
weight: 10
url: /es/python-net/basic-text-extraction/
description: Esta sección contiene artículos sobre la extracción básica de texto de documentos PDF usando Aspose.PDF en Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Extraer texto de todas las páginas de un documento PDF

Aspose.PDF para Python te enseña cómo extraer texto de cada página de un documento PDF. Utiliza la clase TextAbsorber para capturar todo el contenido textual del documento completo y lo guarda en un archivo de texto separado.
Ideal para convertir PDFs en texto buscable, realizar análisis de contenido o exportar texto para tareas de indexación y procesamiento.

1. Cargar el archivo PDF.
1. Crear un objeto 'TextAbsorber'.
1. Llamar a 'document.pages.accept(text_absorber)' para que escanee todas las páginas.
1. Obtener el texto completo mediante 'text_absorber.text'.
1. Escribir el resultado en un archivo de texto.

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
    try:
        # Create a TextAbsorber to extract text
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber for all pages
        document.pages.accept(text_absorber)
        # Get extracted text
        extracted_text = text_absorber.text
        # Write the text to an output file
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## Extraer texto de una página en particular

Extraer texto de una sola página de un documento PDF. Al aplicar TextAbsorber solo a una página especificada, puedes aislar y guardar el texto de una sección particular de un PDF de varias páginas.

Útil cuando solo necesitas contenido de una página, por ejemplo, extrayendo texto de la página de una factura, sección de un informe o resumen de campos de un formulario.

1. Abrir el PDF.
1. Crear un TextAbsorber.
1. Aceptar solo la página designada (pages[page_number]).
1. Extraer texto y escribirlo en un archivo.

```python

import os
import aspose.pdf as ap

def extract_text_from_page(infile, page_number, outfile):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based page index to extract.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber on only the specified page
        document.pages[page_number].accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

