---
title: Combinar archivos PDF en Python
linktitle: Combinar archivos PDF
type: docs
weight: 50
url: /es/python-net/merge-pdf-documents/
description: Aprende cómo combinar varios archivos PDF en un solo documento en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combina páginas PDF usando Python
Abstract: Este artículo aborda la necesidad común de combinar varios archivos PDF en un solo documento, un proceso valioso para organizar y optimizar el almacenamiento y la compartición del contenido PDF. Explora el uso de Aspose.PDF for Python via .NET para combinar eficientemente archivos PDF, reconociendo que la fusión de PDFs en Python puede ser un desafío sin bibliotecas de terceros. El artículo proporciona una guía paso a paso para concatenar archivos PDF: crear un nuevo documento, combinar los archivos y guardar el documento combinado. Un fragmento de código demuestra la implementación usando Aspose.PDF, destacando la capacidad de la biblioteca para simplificar el proceso de fusión. Además, presenta Aspose.PDF Merger, una herramienta en línea para combinar PDFs, que permite a los usuarios explorar la funcionalidad en un entorno web.
---

## Combinar o fusionar varios PDF en un único PDF en Python

Combinar archivos PDF es una consulta muy popular entre los usuarios Esto puede ser útil cuando tienes varios archivos PDF que deseas compartir o almacenar juntos como un solo documento.

Combinar archivos PDF puede ayudarle a organizar sus documentos, liberar espacio de almacenamiento en su PC y compartir varios archivos PDF con otros al combinarlos en un solo documento.

Fusionar PDF en Python a través de .NET no es una tarea sencilla sin usar una biblioteca de terceros.
Este artículo muestra cómo combinar varios archivos PDF en un único documento PDF usando Aspose.PDF for Python via .NET. 

## Fusionar archivos PDF usando Python y DOM

Para concatenar dos archivos PDF:

1. Crear un nuevo documento.
1. Combinar los archivos PDF
1. Guardar el documento combinado

Combinar varios documentos PDF en un solo archivo:

```python
import sys
import aspose.pdf as ap
from os import path


def merge_two_documents(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## Añadir un rango de páginas de un PDF a otro

Copiar y agregar un rango específico de páginas de un documento PDF de origen a un documento PDF de destino utilizando Aspose.PDF for Python.

1. Abre los archivos PDF usando la clase Document.
1. Verifique si el documento fuente tiene páginas.
1. Validar el rango de páginas.
1. Omita la operación si la página inicial es mayor que la página final.
1. Iterar a través del rango de páginas.
1. Añadir páginas al documento de destino.

```python
import sys
import aspose.pdf as ap
from os import path


def _append_page_range(source_document, destination_document, start_page, end_page):
    total_pages = len(source_document.pages)
    if total_pages == 0:
        return

    start = max(1, start_page)
    end = min(end_page, total_pages)
    if start > end:
        return

    for page_number in range(start, end + 1):
        destination_document.pages.add(source_document.pages[page_number])
```

## Combinar varios documentos PDF en uno

Este fragmento de código explica cómo combinar varios archivos PDF en un solo documento:

1. Crea un documento de salida vacío.
1. Itera a través de los archivos de entrada.
1. Cargue cada documento de origen.
1. Determinar el rango de páginas.
1. Agregar páginas al documento de salida.
1. Repita para todos los documentos.
1. Guardar el PDF fusionado.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_multiple_documents(input_files, outfile):
    output_document = ap.Document()

    for input_file in input_files:
        source_document = ap.Document(input_file)
        _append_page_range(
            source_document, output_document, 1, len(source_document.pages)
        )

    output_document.save(outfile)
```

## Combinar rangos de páginas seleccionados de varios PDF

1. Cargar los documentos PDF de origen.
1. Crear un documento de salida.
1. Definir rangos de páginas para cada documento.
1. Agregar páginas del primer documento.
1. Añadir páginas del segundo documento.
1. Combina las páginas en el orden deseado.
1. Guardar el PDF fusionado.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_selected_page_ranges(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    output_document = ap.Document()

    _append_page_range(document1, output_document, 1, 2)
    _append_page_range(document2, output_document, 2, 3)

    output_document.save(outfile)
```

## Insertar un PDF en otro en una posición específica

1. Cargue la base e inserte los documentos.
1. Crear un documento de salida.
1. Determinar el total de páginas en el documento base.
1. Validar el índice de inserción.
1. Agregar páginas antes del punto de inserción.
1. Añadir todas las páginas del documento insertado.
1. Agregar las páginas restantes del documento base.
1. Guarda el PDF resultante.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_insert_document_at_position(infile1, infile2, insert_after_page, outfile):
    base_document = ap.Document(infile1)
    insert_document = ap.Document(infile2)
    output_document = ap.Document()

    base_total_pages = len(base_document.pages)
    insert_index = max(0, min(insert_after_page, base_total_pages))

    _append_page_range(base_document, output_document, 1, insert_index)
    _append_page_range(insert_document, output_document, 1, len(insert_document.pages))
    _append_page_range(
        base_document, output_document, insert_index + 1, base_total_pages
    )

    output_document.save(outfile)
```

## Combinar PDFs alternando páginas

Este ejemplo demuestra cómo combinar dos documentos PDF alternando sus páginas usando Aspose.PDF for Python.

1. Cargue los documentos PDF de entrada.
1. Crear un documento de salida.
1. Obtenga el número de páginas en cada documento.
1. Calcule el número máximo de páginas.
1. Iterar sobre los números de página.
1. Agregar páginas alternadamente.
1. Manejar recuentos de páginas desiguales.
1. Guardar el PDF fusionado.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_alternating_pages(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    output_document = ap.Document()

    document1_pages = len(document1.pages)
    document2_pages = len(document2.pages)
    max_pages = max(document1_pages, document2_pages)

    for page_number in range(1, max_pages + 1):
        if page_number <= document1_pages:
            output_document.pages.add(document1.pages[page_number])
        if page_number <= document2_pages:
            output_document.pages.add(document2.pages[page_number])

    output_document.save(outfile)
```

## Combinar PDFs con separadores de sección y marcadores

Combina varios documentos PDF en un único archivo con secciones estructuradas y marcadores de navegación usando Aspose.PDF for Python.

1. Crear un documento de salida.
1. Itera a través de los archivos de entrada.
1. Cargar el documento fuente.
1. Agregar una página separadora.
1. Crear un marcador de sección.
1. Agregar páginas del documento de origen.
1. Rastrear la primera página de contenido.
1. Agregar un marcador de contenido anidado (opcional).
1. Repita para todos los documentos.
1. Guardar el PDF fusionado.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_with_section_separators_and_bookmarks(input_files, outfile):
    output_document = ap.Document()

    for section_index, input_file in enumerate(input_files, start=1):
        source_document = ap.Document(input_file)
        source_page_count = len(source_document.pages)

        separator_page = output_document.pages.add()
        separator_page.paragraphs.add(
            ap.text.TextFragment(
                f"Section {section_index}: {path.basename(input_file)}"
            )
        )

        section_bookmark = ap.OutlineItemCollection(output_document.outlines)
        section_bookmark.title = f"Section {section_index}"
        section_bookmark.action = ap.annotations.GoToAction(separator_page)
        output_document.outlines.append(section_bookmark)

        first_content_page_number = len(output_document.pages) + 1
        _append_page_range(source_document, output_document, 1, source_page_count)

        if source_page_count > 0 and first_content_page_number <= len(
            output_document.pages
        ):
            content_bookmark = ap.OutlineItemCollection(output_document.outlines)
            content_bookmark.title = f"Section {section_index} Content"
            content_bookmark.action = ap.annotations.GoToAction(
                output_document.pages[first_content_page_number]
            )
            section_bookmark.append(content_bookmark)

    output_document.save(outfile)
```

## Ejemplo en vivo

[Aspose.PDF Fusionador](https://products.aspose.app/pdf/merger) es una aplicación web gratuita en línea que le permite investigar cómo funciona la funcionalidad de fusión de presentaciones.

[![Aspose.PDF Fusionador](merger.png)](https://products.aspose.app/pdf/merger)

## Temas de documentos relacionados

- [Trabajar con documentos PDF en Python](/pdf/es/python-net/working-with-documents/)
- [Dividir archivos PDF en Python](/pdf/es/python-net/split-document/)
- [Optimizar archivos PDF en Python](/pdf/es/python-net/optimize-pdf/)
- [Manipular documentos PDF en Python](/pdf/es/python-net/manipulate-pdf-document/)

