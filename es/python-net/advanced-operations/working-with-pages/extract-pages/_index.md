---
title: Extraer páginas PDF en Python
linktitle: Extrayendo páginas PDF
type: docs
weight: 80
url: /es/python-net/extract-pages/
description: Aprende cómo extraer una o varias páginas PDF en nuevos archivos con Python.
lastmod: "2026-04-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer páginas PDF usando Python
Abstract: Este artículo explica cómo extraer páginas de archivos PDF usando Aspose.PDF for Python via .NET. Aprende cómo copiar una página individual o varias páginas en un nuevo documento utilizando la indexación de páginas basada en 1 y la API PageCollection.
---

## Extraer una sola página de un PDF

Extrae una página específica de un documento PDF y guárdala como un archivo nuevo. Usando la biblioteca Aspose.PDF, el script copia la página deseada a un nuevo PDF, dejando el documento original sin cambios. Esto es útil para dividir PDFs o aislar páginas importantes para su distribución.

1. Cargue el PDF de origen usando el [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. Crear un nuevo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para contener la página extraída.
1. Añada el deseado [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) del documento de origen al nuevo PDF usando el documento de destino [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (`dst_document.pages.add(...)`).
    - En este ejemplo, la página 2 se extrae (indexación basada en 1).
1. Guarda el nuevo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con la página extraída al archivo de salida especificado.

```python
import aspose.pdf as ap

def extract_page(input_file_name: str, output_file_name: str) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    dst_document.pages.add(src_document.pages[2])
    dst_document.save(output_file_name)
```

## Extraer varias páginas de un PDF

Extraiga varias páginas específicas de un documento PDF y guárdelas en un nuevo archivo. Con la biblioteca Aspose.PDF, las páginas seleccionadas se copian a un nuevo PDF mientras se mantiene intacto el documento original. Esto es útil para crear PDFs más pequeños que contengan solo las secciones relevantes de un documento más grande.

1. Cargue el PDF de origen usando el [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. Crear un nuevo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para contener las páginas extraídas.
1. Seleccione las páginas a extraer (en este ejemplo, páginas 2 y 3 usando indexación basada en 1).
1. Agregue cada seleccionado [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) del documento fuente al nuevo PDF usando su [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Guarda el nuevo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con las páginas extraídas al archivo de salida especificado.

```python
import aspose.pdf as ap

def extract_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    pages = [2, 3]
    another_document = ap.Document()
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    another_document.save(output_file_name)
```

## Temas de página relacionados

- [Trabajar con páginas PDF en Python](/pdf/es/python-net/working-with-pages/)
- [Eliminar páginas PDF en Python](/pdf/es/python-net/delete-pages/)
- [Mover páginas PDF en Python](/pdf/es/python-net/move-pages/)
- [Dividir archivos PDF en Python](/pdf/es/python-net/split-document/)
