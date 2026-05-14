---
title: Eliminar imágenes de archivo PDF usando Python
linktitle: Eliminar imágenes
type: docs
weight: 20
url: /es/python-net/delete-images-from-pdf-file/
description: Aprenda cómo eliminar imágenes específicas o todas las imágenes de archivos PDF en Python.
lastmod: "2026-05-05"
TechArticle: true
AlternativeHeadline: Eliminar imágenes de archivos PDF con Python
Abstract: Este artículo muestra cómo eliminar imágenes de documentos PDF con Aspose.PDF for Python via .NET. Cubre la eliminación de un recurso de imagen específico y la eliminación de todas las imágenes de una página seleccionada.
---

Utilice esta página cuando necesite eliminar gráficos innecesarios, reducir el tamaño del PDF o limpiar contenido visual sensible de un documento.

## Eliminar imágenes del archivo PDF

Utilice los siguientes pasos para eliminar una imagen de una página:

1. Cargar el PDF de origen con `ap.Document(infile)`.
1. Seleccione la página y el índice del recurso de imagen.
1. Eliminar la imagen con `resources.images.delete(index)`.
1. Guarda el PDF actualizado.

```python
import aspose.pdf as ap


def delete_image(infile, outfile):
    document = ap.Document(infile)
    document.pages[1].resources.images.delete(1)
    document.save(outfile)
```

## Eliminar todas las imágenes de una página

Utilice este ejemplo para eliminar cada imagen de una página específica.

```python
import aspose.pdf as ap


def delete_all_images_from_page(infile, outfile, page_number):
    document = ap.Document(infile)
    page = document.pages[page_number]

    while len(page.resources.images) != 0:
        page.resources.images.delete(1)

    document.save(outfile)
```

## Temas de imágenes relacionadas

- [Trabajar con imágenes en PDF usando Python](/pdf/es/python-net/working-with-images/)
- [Reemplazar imágenes en archivos PDF existentes](/pdf/es/python-net/replace-image-in-existing-pdf-file/)
- [Extraer imágenes de archivos PDF](/pdf/es/python-net/extract-images-from-pdf-file/)
- [Agregar imágenes a archivos PDF existentes](/pdf/es/python-net/add-image-to-existing-pdf-file/)