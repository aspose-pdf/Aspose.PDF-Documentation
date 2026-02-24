---
title: Agregar páginas en PDF con Python
linktitle: Agregar páginas
type: docs
weight: 10
url: /es/python-net/add-pages/
description: Descubre cómo agregar páginas a un documento PDF en Python usando Aspose.PDF para una creación y edición flexible de documentos.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar páginas en PDF usando Python
Abstract: El artículo ofrece una guía sobre el uso de Aspose.PDF para Python a través de la API .NET para manipular páginas en un documento PDF. Destaca la flexibilidad que brinda la API, particularmente mediante la clase `PageCollection`, que gestiona todas las páginas dentro de un PDF. El documento detalla los procedimientos para agregar o insertar páginas en ubicaciones específicas de un archivo PDF. Describe dos operaciones principales insertar una página vacía en la ubicación deseada dentro del documento y agregar una página vacía al final del documento. Para ambas operaciones, el proceso consiste en crear un objeto `Document`, usar los métodos `insert` o `add` de `PageCollection` y guardar el documento modificado. El artículo incluye fragmentos de código que demuestran estas tareas, mostrando lo sencillo que es manipular documentos PDF usando Python con esta API.
---

Aspose.PDF para Python a través de la API .NET proporciona total flexibilidad para trabajar con páginas en un documento PDF usando Python. Mantiene todas las páginas de un documento PDF en [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) que pueden usarse para trabajar con páginas PDF.
Aspose.PDF para Python a través de .NET le permite insertar una página en un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) en cualquier ubicación del archivo, así como añadir páginas al final de un archivo PDF. Esta sección muestra cómo agregar páginas a un PDF usando Python.

## Agregar o Insertar Página en un Archivo PDF

Aspose.PDF para Python a través de .NET le permite insertar una página en un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) en cualquier ubicación del archivo, así como añadir páginas al final de un archivo PDF.

### Insertar Página Vacía en un Archivo PDF

Para insertar una página vacía en un archivo PDF:

1. Abra un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) existente mediante los métodos adecuados.
1. Inserte una nueva página vacía en un índice específico usando el método `insert()` de la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Guarde el [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modificado en la ruta de salida deseada.

Inserte una página vacía en un archivo PDF existente en una posición especificada:

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def insert_empty_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### Añadir una Página Vacía al Final de un Archivo PDF

A veces, desea asegurarse de que un documento termine en una página vacía. Este tema explica cómo insertar una página vacía al final del documento PDF.

Para insertar una página vacía al final de un archivo PDF:

1. Abra un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) existente mediante los métodos adecuados.
1. Añada una nueva página vacía al final del documento usando el método `add()` de la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Guarde el [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) actualizado.

El siguiente fragmento de código le muestra cómo insertar una página vacía al final de un archivo PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_empty_page_to_end(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Insert an empty page at the end of a PDF file
    document.pages.add()

    # Save output file
    document.save(output_file_name)
```

### Añadir una Página desde Otro Documento PDF

Con la biblioteca Aspose.PDF para Python, crea un nuevo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), agrega una página inicial y luego importa una página de otro PDF en él.

1. Cree un nuevo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Añada una nueva [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) en blanco y escriba algún texto en ella usando [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/).
1. Abra otro [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) existente.
1. Copie una [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) de ese documento.
1. Pegue la página copiada en su documento principal usando [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Guarde el archivo combinado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_from_another_document(input_file_name, output_file_name):
    # Open document
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    # Save output file
    document.save(output_file_name)
```
