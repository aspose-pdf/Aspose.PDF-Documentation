---
title: Eliminar páginas PDF en Python
linktitle: Eliminando páginas PDF
type: docs
weight: 80
url: /es/python-net/delete-pages/
description: Aprende cómo eliminar páginas de archivos PDF en Python.
lastmod: "2026-04-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar una o más páginas PDF en Python
Abstract: Este artículo explica cómo eliminar páginas de archivos PDF usando Aspose.PDF for Python via .NET. Aprende cómo eliminar una sola página o varias páginas de un documento usando la API PageCollection y luego guarda el PDF actualizado.
---

Puedes eliminar páginas de un archivo PDF usando Aspose.PDF for Python via .NET. Para eliminar una página en particular, usa el [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) de un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Utilice este flujo de trabajo cuando necesite eliminar páginas no deseadas de un PDF antes de compartir, archivar o combinar documentos.

## Eliminar página del archivo PDF

Aspose.PDF for Python via .NET elimina la página 2 del PDF de entrada y guarda el documento actualizado en un nuevo archivo. Esta característica es útil para eliminar páginas no deseadas o sensibles sin alterar el resto del documento.

1. Cargue el PDF de entrada como un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Elimine la página usando el [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Llame al [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método para guardar el archivo PDF actualizado.

El siguiente fragmento de código muestra cómo eliminar una página concreta del archivo PDF usando Python.

```python
import aspose.pdf as ap

def delete_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.delete(2)
    document.save(output_file_name)
```

## Eliminar varias páginas de un documento PDF

Eliminar varias páginas permite eliminar un conjunto de páginas especificadas en una única operación, lo que es más eficiente que eliminar páginas una por una. El PDF resultante se guarda en un nuevo archivo, preservando el documento original.

1. Cargue el PDF de entrada como un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Elimina las páginas enumeradas en la matriz pages usando el [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Guardar lo actualizado [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) a un nuevo archivo.

```python
import aspose.pdf as ap

def delete_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    # Example: delete pages 2, 3, and 4.
    pages = [2, 3, 4]
    document.pages.delete(pages)
    document.save(output_file_name)
```

## Temas de página relacionados

- [Trabajar con páginas PDF en Python](/pdf/es/python-net/working-with-pages/)
- [Agregar páginas PDF en Python](/pdf/es/python-net/add-pages/)
- [Mover páginas PDF en Python](/pdf/es/python-net/move-pages/)
- [Extraer páginas PDF en Python](/pdf/es/python-net/extract-pages/)
