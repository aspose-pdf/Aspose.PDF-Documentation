---
title: Mover páginas PDF programáticamente mediante Python
linktitle: Mover páginas PDF
type: docs
weight: 100
url: /es/python-net/move-pages/
description: Intenta mover páginas a la ubicación deseada o al final de un archivo PDF usando Aspose.PDF para Python a través de .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mover páginas entre documentos PDF usando Python
Abstract: El artículo ofrece una guía completa sobre cómo mover páginas entre documentos PDF o dentro de un único documento PDF utilizando Python, específicamente mediante la biblioteca Aspose.PDF. Describe procesos paso a paso para tres escenarios mover una sola página de un PDF a otro, transferir varias páginas y reubicar una página dentro del mismo documento. Cada escenario implica crear objetos de clase `Document` para los PDFs de origen y destino, manipular páginas a través de la clase `PageCollection` y utilizar los métodos `add`, `delete` y `save` para lograr la reorganización de páginas deseada. Se proporcionan fragmentos de código para una implementación práctica, demostrando cómo mover páginas de manera eficiente usando scripts de Python.
---

## Mover una página de un documento PDF a otro

Aspose.PDF for Python permite mover una página (no solo copiarla) de un PDF a otro. Elimina la página seleccionada del documento original y luego la agrega a un nuevo archivo PDF.

Piénsalo como cortar una página de un libro y pegarla en otro: la página ya no existe en el archivo original después del movimiento.

1. Abre el documento PDF fuente utilizando la clase [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Selecciona una página específica para mover (en este caso, la página 2) — esto se refiere a una [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Crea un nuevo documento PDF (instancia otra [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Añade la página seleccionada al nuevo documento PDF usando la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) del documento de destino (por ejemplo, `another_document.pages.add(page)`).
1. Elimina la página del documento original a través de su [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (por ejemplo, `document.pages.delete(index)`).
1. Guarda ambos documentos.

El siguiente fragmento de código muestra cómo mover una página.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a single page from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf","_new.pdf"))
    another_document.save(output_file_name)
```

## Mover un conjunto de páginas de un documento PDF a otro

A diferencia de copiar, esta operación transfiere las páginas seleccionadas — eliminándolas del archivo origen y guardándolas en un nuevo PDF.

1. Crea un nuevo documento de destino vacío (`Document`).
1. Selecciona varias páginas (en este caso, las páginas 1 y 3) de la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) del documento fuente.
1. Recorre las páginas seleccionadas y añade cada una a la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) del documento de destino.
1. Guarda el documento de destino que contiene las páginas movidas.
1. Elimina las páginas movidas del documento origen utilizando su [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Guarda el documento origen modificado con un nuevo nombre de archivo para conservar ambas versiones.

El siguiente fragmento de código muestra cómo insertar una página en blanco al final de un archivo PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_bunch_pages_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a set of pages from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file where selected pages will be saved.
    """
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf","_new.pdf"))
```

## Mover una página a una nueva ubicación en el documento PDF actual

Muestra cómo mover una página específica a una posición diferente dentro del mismo documento — una necesidad frecuente al reorganizar o editar diseños de PDF.

1. Carga el documento PDF de entrada utilizando la clase [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Selecciona la página que deseas mover (página 2) — esto es una [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Añádela al final del documento usando la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) del documento.
1. Elimina la página original de su ubicación anterior a través de la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Guarda el documento modificado como un nuevo archivo.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_in_new_location_in_same_document(input_file_name, output_file_name):
    """
    Move a page to a new location within the same PDF document.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    srcDocument = ap.Document(input_file_name)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # Save output file
    srcDocument.save(output_file_name)
```


