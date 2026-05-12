---
title: Mover páginas PDF en Python
linktitle: Mover páginas PDF
type: docs
weight: 100
url: /es/python-net/move-pages/
description: Aprenda cómo mover páginas PDF dentro de un documento o entre documentos en Python.
lastmod: "2026-04-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mover páginas PDF entre documentos en Python
Abstract: Este artículo explica cómo mover páginas en PDFs usando Aspose.PDF for Python via .NET. Aprende cómo mover una sola página o varias páginas a otro documento, y cómo reubicar una página dentro del mismo PDF usando las APIs Document y PageCollection.
---

## Mover una página de un documento PDF a otro

Aspose.PDF for Python le permite mover una página (no solo copiarla) de un PDF a otro. Elimina la página seleccionada del documento original y luego la agrega a un nuevo archivo PDF.

Piense en ello como cortar una página de un libro y pegarla en otro — la página ya no existe en el archivo original después del movimiento.

1. Abra el documento PDF de origen usando el [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase.
1. Seleccione una página específica para mover (en este caso, la página 2) — esto se refiere a un [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Cree un nuevo documento PDF (instancie otro [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Agregue la página seleccionada al nuevo documento PDF usando el documento de destino [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (por ejemplo, `another_document.pages.add(page)`).
1. Elimine la página del documento original mediante su [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (por ejemplo, `document.pages.delete(index)`).
1. Guarde ambos documentos.

El siguiente fragmento de código le muestra cómo mover una página.

```python
import aspose.pdf as ap

def move_page_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:

    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf", "_new.pdf"))
    another_document.save(output_file_name)
```

## Mover varias páginas de un documento PDF a otro

A diferencia de copiar, esta operación transfiere las páginas seleccionadas — eliminándolas del archivo origen y guardándolas en un nuevo PDF.

1. Crear un nuevo documento de destino vacío (`Document`).
1. Seleccione varias páginas (en este caso, las páginas 1 y 3) del documento de origen [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Recorra las páginas seleccionadas y agregue cada una al documento de destino [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Guarda el documento de destino que contiene las páginas movidas.
1. Elimina las páginas movidas del documento origen usando su [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Guarda el documento origen modificado con un nuevo nombre de archivo para conservar ambas versiones.

El siguiente fragmento de código muestra cómo mover varias páginas.

```python
import aspose.pdf as ap

def move_multiple_pages_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 2]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf", "_new.pdf"))
```

## Mover una página a una nueva ubicación en el mismo documento PDF

Muestra cómo mover una página específica a una posición diferente dentro del mismo documento — una necesidad común al reorganizar o editar diseños de PDF.

1. Cargue el documento PDF de entrada usando el [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase.
1. Seleccione la página que desea mover (página 2) — esto es un [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Agrégala al final del documento usando el documento [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Eliminar la página original de su ubicación anterior a través de la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Guardar el documento modificado como un archivo nuevo.

```python
import aspose.pdf as ap

def move_page_in_new_location_in_same_document(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)

    page = src_document.pages[2]
    src_document.pages.add(page)
    src_document.pages.delete(2)

    # Save output file
    src_document.save(output_file_name)
```

## Temas de página relacionados

- [Trabajar con páginas PDF en Python](/pdf/es/python-net/working-with-pages/)
- [Agregar páginas PDF en Python](/pdf/es/python-net/add-pages/)
- [Eliminar páginas PDF en Python](/pdf/es/python-net/delete-pages/)
- [Extraer páginas PDF en Python](/pdf/es/python-net/extract-pages/)
