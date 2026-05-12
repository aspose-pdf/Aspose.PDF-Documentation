---
title: Dividir archivos PDF en Python
linktitle: Dividir archivos PDF
type: docs
weight: 60
url: /es/python-net/split-pdf-document/
description: Aprende cómo dividir páginas PDF en archivos PDF separados en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dividir páginas PDF usando Python
Abstract: El artículo analiza el proceso de dividir páginas PDF en archivos individuales usando Python, resaltando la utilidad de dicha función para gestionar documentos PDF grandes. Hace referencia al Aspose.PDF Splitter, una herramienta en línea diseñada para demostrar la funcionalidad de división de PDF. El artículo proporciona un método detallado para lograr esto en aplicaciones Python, que implica iterar a través de las páginas de un documento PDF mediante la `PageCollection` del objeto `Document`. Para cada página, se crea un nuevo objeto `Document`, se añade la página a este, y el nuevo archivo PDF se guarda usando el método `save()`. Un fragmento de código Python adjunto ilustra este proceso, mostrando los pasos necesarios para dividir un documento PDF en archivos separados iterando sus páginas y guardando cada una como un PDF individual.
---

Dividir páginas PDF puede ser una característica útil para quienes desean dividir un archivo grande en páginas separadas o grupos de páginas.

Utilice este flujo de trabajo cuando necesite dividir archivos PDF grandes en archivos de una sola página o en conjuntos de documentos más pequeños para distribución, revisión o procesamiento posterior.

## Ejemplo en vivo

[Divisor de Aspose.PDF](https://products.aspose.app/pdf/splitter) es una aplicación web gratuita en línea que le permite investigar cómo funciona la funcionalidad de división de presentaciones.

[![Aspose Dividir PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Este tema muestra cómo dividir páginas PDF en archivos PDF individuales en sus aplicaciones Python. Para dividir páginas PDF en archivos PDF de una sola página usando Python, se pueden seguir los siguientes pasos:

1. Recorrer las páginas del documento PDF a través de la [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) del objeto [ColecciónDePáginas](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) colección
1. Para cada iteración, crea un nuevo objeto Document y agrega el individual [Página](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) objeto en el documento vacío
1. Guardar el nuevo PDF usando [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método

## Dividir PDF en varios archivos o pdfs separados en Python

El siguiente fragmento de código Python le muestra cómo dividir las páginas PDF en archivos PDF individuales.

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

## Dividir un PDF en dos partes iguales

1. Cargue el documento PDF.
1. Determinar el número total de páginas.
1. Calcule el punto medio.
1. Crea el primer documento de salida.
1. Eliminar las páginas de la segunda mitad del primer documento.
1. Guarda la primera parte.
1. Cree el segundo documento de salida.
1. Eliminar las páginas de la primera mitad del segundo documento.
1. Guardar la segunda parte.

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

Divida un documento PDF en varios archivos más pequeños basándose en un número fijo de páginas usando Aspose.PDF for Python via .NET.

1. Cargue el documento PDF.
1. Determinar el número total de páginas.
1. Definir páginas por parte.
1. Itera a través del documento en fragmentos.
1. Calcule el rango de páginas para cada parte.
1. Crea un nuevo documento para cada parte.
1. Copiar páginas al nuevo documento.
1. Guarda el documento dividido.
1. Repita hasta que se procesen todas las páginas.

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

## Dividir un PDF por rangos de página personalizados

Dividir un documento PDF en varios archivos basados en rangos de páginas personalizados usando Aspose.PDF for Python.

1. Cargue el documento PDF.
1. Determinar el número total de páginas.
1. Crea una lista de tuplas que representen rangos (start_page, end_page).
1. Iterar a través de los rangos definidos.
1. Validar la página de inicio.
1. Ajusta la página final.
1. Validar el rango efectivo.
1. Cree un nuevo documento para cada rango.
1. Copiar páginas al nuevo documento.
1. Guarde cada documento dividido.

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

## Dividir un PDF en Primera página y Páginas restantes

Separe la primera página de un documento PDF del resto de las páginas usando Aspose.PDF for Python.

1. Cargue el documento PDF.
1. Determinar el número total de páginas.
1. Verifique si el documento está vacío.
1. Crea un documento para la primera página.
1. Agregar la primera página.
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

1. Cargue el documento PDF.
1. Determinar el número total de páginas.
1. Verifique si el documento está vacío.
1. Crea un documento para la última página.
1. Agregar la última página.
1. Guarda el documento de la última página.
1. Verificar documentos de una sola página.
1. Elimina la última página del documento original.
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

Divida un documento PDF en tres partes separadas usando Aspose.PDF for Python.

1. Cargue el documento PDF.
1. Determinar el número total de páginas.
1. Verifique si el documento está vacío.
1. Calcular el tamaño de la pieza.
1. Iterar a través de tres partes.
1. Determine el rango de páginas para cada parte.
1. Validar el rango de páginas.
1. Crea un nuevo documento para cada parte.
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

Divida un documento PDF en varios archivos basándose en grupos de páginas definidos de forma personalizada usando Aspose.PDF for Python.

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

Divida un documento PDF en páginas individuales y guárdelas con nombres de archivo estables utilizando Aspose.PDF for Python.

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

Divida un documento PDF en dos archivos separados que contengan, respectivamente, las páginas impares y pares, usando Aspose.PDF for Python via .NET.

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

## Temas de documentos relacionados

- [Trabajar con documentos PDF en Python](/pdf/es/python-net/working-with-documents/)
- [Fusionar archivos PDF en Python](/pdf/es/python-net/merge-pdf-documents/)
- [Optimizar archivos PDF en Python](/pdf/es/python-net/optimize-pdf/)
- [Manipular documentos PDF en Python](/pdf/es/python-net/manipulate-pdf-document/)

