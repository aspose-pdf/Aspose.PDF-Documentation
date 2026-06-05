---
title: Dividir archivos PDF en Python
linktitle: Dividir archivos PDF
type: docs
weight: 60
url: /es/python-net/split-pdf-document/
description: Aprenda cómo dividir archivos PDF en Python en páginas individuales, partes iguales, grupos de tamaño fijo, rangos de páginas personalizados y páginas impares o pares.
lastmod: "2026-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Divida PDF en páginas y rangos de páginas usando Python.
Abstract: Este artículo muestra cómo dividir archivos PDF con Aspose.PDF for Python via .NET. Cubre la división de un PDF en páginas individuales, dos partes iguales, grupos de páginas de tamaño fijo, rangos de páginas personalizados, grupos de páginas con nombre, nombres de archivo estables y archivos de páginas impares o pares.
---

Esta página muestra cómo **dividir archivos PDF en Python** usando Aspose.PDF for Python via .NET.

Utiliza estos ejemplos cuando necesites dividir un PDF grande en archivos de una sola página, partes iguales, grupos de tamaño fijo, rangos de páginas personalizados, o conjuntos de páginas impares y pares para distribución, revisión o procesamiento posterior.

## Ejemplo de división de PDF en línea

[Divisor de Aspose.PDF](https://products.aspose.app/pdf/splitter) es una aplicación web en línea que permite probar la funcionalidad de división de PDF.

[![Dividir PDF con Aspose](splitter.png)](https://products.aspose.app/pdf/splitter)

Para dividir las páginas de PDF en archivos PDF de una sola página en Python, siga estos pasos:

1. Recorrer las páginas del documento PDF a través del [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) del objeto [Colección de páginas](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) colección
1. Para cada iteración, crea un nuevo objeto Document y agrega el individual [Página](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) objeto en el documento vacío
1. Guardar el nuevo PDF usando [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método

## Dividir PDF en varios archivos en Python

El siguiente fragmento de código Python le muestra cómo dividir las páginas de PDF en archivos PDF individuales.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents(infile, outdir):
    document = ap.Document(infile)
    for page_num in range(1, len(document.pages) + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num}.pdf"))
```

## Dividir un PDF en Dos Partes Iguales

1. Cargar el documento PDF.
1. Determinar el número total de páginas.
1. Calcula el punto medio.
1. Crea el primer documento de salida.
1. Eliminar las páginas de la segunda mitad del primer documento.
1. Guarda la primera parte.
1. Crea el segundo documento de salida.
1. Eliminar las páginas de la primera mitad del segundo documento.
1. Guarda la segunda parte.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_two_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    mid_point = total_pages // 2

    # First part
    with ap.Document(infile) as first_document:
        first_part_range = range(mid_point + 1, total_pages + 1)
        first_document.pages.delete(first_part_range)
        first_document.save(path.join(outdir, "Part_1.pdf"))

    # Second part
    with ap.Document(infile) as second_document:
        second_part_range = range(1, mid_point + 1)
        second_document.pages.delete(second_part_range)
        second_document.save(path.join(outdir, "Part_2.pdf"))
```

## Dividir un PDF en varios archivos cada N páginas

Dividir un documento PDF en varios archivos más pequeños basándose en un número fijo de páginas usando Aspose.PDF for Python.

1. Cargar el documento PDF.
1. Determinar el número total de páginas.
1. Definir páginas por parte.
1. Iterar a través del documento en fragmentos.
1. Calcula el rango de páginas para cada parte.
1. Cree un nuevo documento para cada parte.
1. Copiar páginas en el nuevo documento.
1. Guarda el documento dividido.
1. Repita hasta que todas las páginas se procesen.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_every_n_pages(infile, outdir, pages_per_part=3):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    part_index = 1
    for start_page in range(1, total_pages + 1, pages_per_part):
        end_page = min(start_page + pages_per_part - 1, total_pages)

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(
                path.join(outdir, f"Every_{pages_per_part}_Part_{part_index}.pdf")
            )

        part_index += 1
```

## Dividir un PDF por rangos de páginas personalizados

Divida un documento PDF en varios archivos según rangos de páginas personalizados usando Aspose.PDF for Python.

1. Cargar el documento PDF.
1. Determinar el número total de páginas.
1. Cree una lista de tuplas que representen rangos (start_page, end_page).
1. Iterar a través de los intervalos definidos.
1. Validar la página de inicio.
1. Ajusta la página final.
1. Validar el rango efectivo.
1. Crea un nuevo documento para cada rango.
1. Copiar páginas en el nuevo documento.
1. Guarda cada documento dividido.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_by_page_ranges(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    # Define ranges as (start_page, end_page). Use None to indicate last page.
    ranges = [(1, 3), (4, 6), (7, None)]

    for index, (start_page, end_page) in enumerate(ranges, start=1):
        if start_page > total_pages:
            continue

        effective_end = total_pages if end_page is None else min(end_page, total_pages)
        if start_page > effective_end:
            continue

        with ap.Document() as range_document:
            for page_num in range(start_page, effective_end + 1):
                range_document.pages.add(document.pages[page_num])
            range_document.save(
                path.join(outdir, f"Range_{index}_{start_page}_to_{effective_end}.pdf")
            )
```

## Dividir un PDF en la primera página y las páginas restantes

Separar la primera página de un documento PDF del resto de las páginas usando Aspose.PDF for Python.

1. Cargar el documento PDF.
1. Determinar el número total de páginas.
1. Verifique si el documento está vacío.
1. Cree un documento para la primera página.
1. Añade la primera página.
1. Guardar el documento de la primera página.
1. Verifique si hay páginas adicionales.
1. Crea un documento para las páginas restantes.
1. Copiar páginas restantes.
1. Guarda el documento de páginas restantes.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_first_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as first_page_document:
        first_page_document.pages.add(document.pages[1])
        first_page_document.save(path.join(outdir, "First_Page.pdf"))

    if total_pages == 1:
        return

    with ap.Document() as remaining_pages_document:
        for page_num in range(2, total_pages + 1):
            remaining_pages_document.pages.add(document.pages[page_num])
        remaining_pages_document.save(path.join(outdir, "Remaining_Pages.pdf"))
```

## Dividir un PDF en la última página y las páginas anteriores

Extraiga la última página de un documento PDF y sepárela de las páginas restantes usando Aspose.PDF for Python.

1. Cargar el documento PDF.
1. Determinar el número total de páginas.
1. Verifique si el documento está vacío.
1. Crear un documento para la última página.
1. Agregar la última página.
1. Guarda el documento de la última página.
1. Verifique los documentos de una sola página.
1. Elimine la última página del documento original.
1. Guarda las páginas restantes.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_last_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as last_page_document:
        last_page_document.pages.add(document.pages[total_pages])
        last_page_document.save(path.join(outdir, "Last_Page.pdf"))

    if total_pages == 1:
        return

    document.pages.delete(total_pages)  # Remove last page from original document
    document.save(path.join(outdir, "Previous_Pages.pdf"))
```

## Dividir un PDF en tres partes

Divida un documento PDF en tres partes separadas usando Aspose.PDF para Python.

1. Cargar el documento PDF.
1. Determinar el número total de páginas.
1. Verifique si el documento está vacío.
1. Calcular el tamaño de la parte.
1. Iterar a través de tres partes.
1. Determine el rango de páginas para cada parte.
1. Validar el rango de páginas.
1. Cree un nuevo documento para cada parte.
1. Copiar páginas en el documento de la parte.
1. Guarda cada parte.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_three_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    part_size = max(1, (total_pages + 2) // 3)

    for part_index in range(3):
        start_page = part_index * part_size + 1
        end_page = min((part_index + 1) * part_size, total_pages)

        if start_page > total_pages:
            break

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(path.join(outdir, f"Three_Parts_{part_index + 1}.pdf"))
```

## Divisor de páginas PDF personalizado

Divida un documento PDF en varios archivos basándose en grupos de páginas definidos de forma personalizada utilizando Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_custom_page_groups(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    groups = [
        [1, 2, 5],
        [3, 4, 6, 7],
    ]

    for group_index, group in enumerate(groups, start=1):
        valid_pages = [page_num for page_num in group if 1 <= page_num <= total_pages]
        if not valid_pages:
            continue

        with ap.Document() as group_document:
            for page_num in valid_pages:
                group_document.pages.add(document.pages[page_num])
            group_document.save(path.join(outdir, f"Custom_Group_{group_index}.pdf"))
```

## Dividir PDF en páginas individuales con nombres de archivo estables

Dividir un documento PDF en páginas individuales y guardarlas con nombres de archivo estables usando Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_with_stable_filenames(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    for page_num in range(1, total_pages + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num:03d}.pdf"))
```

## Dividir PDF en páginas impares y pares

Divida un documento PDF en dos archivos separados que contengan respectivamente páginas impares y pares usando Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_odd_even_pages(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Odd pages document
    with ap.Document(infile) as document:
        with ap.Document() as odd_document:
            for page_num in range(1, total_pages + 1, 2):
                odd_document.pages.add(document.pages[page_num])
            odd_document.save(path.join(outdir, "Odd_Pages.pdf"))

        with ap.Document() as even_document:
            for page_num in range(2, total_pages + 1, 2):
                even_document.pages.add(document.pages[page_num])
            even_document.save(path.join(outdir, "Even_Pages.pdf"))
```

## Temas relacionados del documento

- [Trabajar con documentos PDF en Python](/pdf/es/python-net/working-with-documents/)
- [Combinar archivos PDF en Python](/pdf/es/python-net/merge-pdf-documents/)
- [Optimizar archivos PDF en Python](/pdf/es/python-net/optimize-pdf/)
- [Manipular documentos PDF en Python](/pdf/es/python-net/manipulate-pdf-document/)

