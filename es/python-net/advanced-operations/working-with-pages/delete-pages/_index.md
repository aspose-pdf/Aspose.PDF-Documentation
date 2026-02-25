---
title: Eliminación de páginas PDF programáticamente con Python
linktitle: Eliminar páginas PDF
type: docs
weight: 80
url: /es/python-net/delete-pages/
description: Puede eliminar páginas de su archivo PDF usando la biblioteca Aspose.PDF para Python a través de .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo eliminar páginas de PDF usando Python
Abstract: Este artículo ofrece una guía concisa sobre cómo eliminar páginas de un archivo PDF usando la biblioteca Aspose.PDF para Python a través de .NET. Se centra en utilizar la clase `PageCollection` para eliminar páginas específicas. El proceso implica invocar el método `delete()` con el índice de la página a eliminar y luego guardar el documento actualizado con el método `save()`. Además, se proporciona un fragmento de código que muestra la eliminación de una página de un archivo PDF, ilustrando el uso de la biblioteca Aspose.PDF en un contexto práctico.
---

Puede eliminar páginas de un archivo PDF usando Aspose.PDF para Python a través de .NET. Para eliminar una página en particular, use el [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) de un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

## Eliminar página del archivo PDF

Aspose.PDF para Python a través de .NET elimina la página 2 del PDF de entrada y guarda el documento actualizado en un nuevo archivo. Esta función es útil para eliminar páginas no deseadas o sensibles sin alterar el resto del documento.

1. Cargue el PDF de entrada como un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Elimine la página usando el [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Llame al método [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) para guardar el archivo PDF actualizado.

El siguiente fragmento de código muestra cómo eliminar una página en particular del archivo PDF usando Python.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def delete_page(input_file_name, output_file_name):
    """
    Delete a single page from a PDF document.

    Demonstrates how to remove a specific page from a PDF document using
    the Aspose.PDF library. This function deletes page 2 from the input
    document and saves the result to a new file.

    Args:
        input_file_name (str): Path to the input PDF file from which to delete a page.
        output_file_name (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Deletes page 2 (1-based indexing) from the document
        - Page numbering is 1-based (page 2 is the second page)
        - The original document is not modified; a new file is created
        - If the document has fewer than 2 pages, this may raise an error

    Example:
        >>> delete_page("input.pdf", "output.pdf")
        # Removes page 2 from input.pdf and saves result as output.pdf
    """
    # Open the PDF as a Document
    document = ap.Document(input_file_name)
    # Delete page using PageCollection API
    document.pages.delete(2)
    # Save updated Document
    document.save(output_file_name)
```

## Eliminar varias páginas de un documento PDF

La eliminación de múltiples páginas le permite remover un conjunto de páginas especificadas en una sola operación, lo que es más eficiente que eliminar páginas una por una. El PDF resultante se guarda en un nuevo archivo, preservando el documento original.

1. Cargue el PDF de entrada como un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Elimine las páginas listadas en el arreglo de páginas usando el [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Guarde el [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) actualizado en un nuevo archivo.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def delete_bunch_pages(input_file_name, output_file_name):
    """
    Delete multiple pages from a PDF document in a single operation.

    Demonstrates bulk page deletion by removing multiple specified pages
    from a PDF document. This is more efficient than deleting pages
    one by one when removing multiple pages.

    Args:
        input_file_name (str): Path to the input PDF file from which to delete pages.
        output_file_name (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Deletes pages 2, 3, 4, 6, 7, and 9 in this example
        - Page numbers are 1-based (page 2 is the second page)
        - Pages are deleted in the order specified in the list
        - The original document is not modified; a new file is created
        - Ensure the document has enough pages to avoid errors
        - Page numbers should be adjusted if the source document has fewer pages

    Example:
        >>> delete_bunch_pages("input.pdf", "output.pdf")
        # Removes pages 2, 3, 4, 6, 7, and 9 from input.pdf
    """
    # Open the PDF as a Document
    document = ap.Document(input_file_name)
    # Example: Deleting pages 2, 3, 4, 6, 7, and 9; modify this list as needed for your use case.
    pages = [2,3,4,6,7,9]
    # Delete pages via PageCollection API
    document.pages.delete(pages)
    # Save updated Document
    document.save(output_file_name)
```

