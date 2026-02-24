---
title: Extracción de páginas programáticamente con Python
linktitle: Extracción de páginas PDF
type: docs
weight: 80
url: /es/python-net/extract-pages/
description: Puedes extraer páginas de tu archivo PDF usando la biblioteca Aspose.PDF para Python vía .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer páginas PDF usando Python
Abstract: Este artículo muestra cómo extraer páginas de un documento PDF usando la biblioteca Aspose.PDF para Python. Las técnicas cubren tanto la extracción de una sola página como la extracción de múltiples páginas, lo que permite a los desarrolladores crear nuevos archivos PDF que contengan solo las páginas seleccionadas. Los ejemplos ilustran cómo acceder a páginas específicas mediante indexación basada en 1, copiarlas a un nuevo documento PDF y guardar los resultados manteniendo intacto el documento original. Estos métodos son útiles para dividir documentos grandes, compartir secciones seleccionadas o crear subconjuntos PDF personalizados para distribución o análisis.
---

## Extraer una sola página de un PDF

Extrae una página específica de un documento PDF y guárdala como un nuevo archivo. Usando la biblioteca Aspose.PDF, el script copia la página deseada a un nuevo PDF, dejando el documento original sin cambios. Esto es útil para dividir PDFs o aislar páginas importantes para su distribución.

1. Carga el PDF de origen usando la API [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (`ap.Document()`).
1. Crea un nuevo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para contener la página extraída.
1. Añade la [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) deseada del documento de origen al nuevo PDF usando la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) del documento de destino (`dst_document.pages.add(...)`).
- En este ejemplo, se extrae la página 2 (indexación basada en 1).
1. Guarda el nuevo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con la página extraída en el archivo de salida especificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_page(input_file_name, output_file_name):
    """
    Extract a single page from a PDF document.

    Demonstrates how to extract a specific page from a PDF document using
    the Aspose.PDF library. This function extracts page 2 from the input
    document and saves it as a new file containing only that page.

    Args:
        input_file_name (str): Path to the input PDF file from which to extract a page.
        output_file_name (str): Path where the extracted page will be saved.

    Returns:
        None: The function creates a new PDF containing the extracted page and saves it to the output path.

    Note:
        - Extracts page 2 (1-based indexing) from the document
        - Page numbering is 1-based (page 2 is the second page)
        - The original document is not modified; a new file is created
        - If the document has fewer than 2 pages, this may raise an error

    Example:
        >>> extract_page("input.pdf", "output.pdf")
        # Extracts page 2 from input.pdf and saves result as output.pdf
    """
    # Open source PDF as Document
    src_document = ap.Document(input_file_name)
    # Create destination Document to hold extracted pages
    dst_document = ap.Document()
    # Add a Page from source to destination using PageCollection API
    dst_document.pages.add(src_document.pages[2])
    # Save destination Document
    dst_document.save(output_file_name)
```

## Extraer múltiples páginas de un PDF

Extrae múltiples páginas específicas de un documento PDF y guárdalas en un nuevo archivo. Usando la biblioteca Aspose.PDF, las páginas seleccionadas se copian a un nuevo PDF dejando el documento original intacto. Esto es útil para crear PDFs más pequeños que contengan solo las secciones relevantes de un documento más grande.

1. Carga el PDF de origen usando la API [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (`ap.Document()`).
1. Crea un nuevo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para contener las páginas extraídas.
1. Selecciona las páginas a extraer (en este ejemplo, las páginas 2 y 3 usando indexación basada en 1).
1. Añade cada [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) seleccionada del documento de origen al nuevo PDF usando su [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Guarda el nuevo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con las páginas extraídas en el archivo de salida especificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_bunch_pages(input_file_name, output_file_name):
    """
    Extract specific pages from a PDF document and save them to a new file.

    This function reads a PDF document, extracts pages 2 and 3 (1-indexed),
    and saves them to a new PDF file.

    Args:
        input_file_name (str): Path to the input PDF file to extract pages from.
        output_file_name (str): Path where the new PDF file with extracted pages will be saved.

    Returns:
        None

    Note:
        The function specifically extracts pages 2 and 3 from the source document.
        Page indexing appears to be 1-based in this implementation.
    """
    # Open source Document
    document = ap.Document(input_file_name)
    pages = [2,3]
    # Create destination Document
    another_document = ap.Document()
    # Copy selected Page objects via PageCollection API
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    # Save destination Document
    another_document.save(output_file_name)
```
